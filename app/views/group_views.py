import datetime
from flask import Blueprint, request, make_response, jsonify
from app import app, swag
from app.models.group_model import Group
from app.models.users import User
from app.models.db import DatabaseConnection
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.handler.validators.message_validators import validate_message, validate_subject
from app.handler.validators.group_validators import check_group_id
from flasgger import swag_from


groups_blueprint = Blueprint('groups', __name__)


@groups_blueprint.route('/groups', methods=['POST'])
@jwt_required
@swag_from('../apidocs/create_group.yml', methods=['POST'])
def create_new_group():
    current_user=get_jwt_identity()
    data_posted = request.get_json(force=True)
    if request.method == "POST":
        new_group=Group(
            group_name=data_posted['group_name'],
            role=data_posted['role'],
            createdby=current_user['email']
        )
        if Group.check_groupname_existance(new_group.group_name):
            return jsonify(
                {
                    "status": 409,
                    "message":"Group name already taken"
                }
            )
        create=new_group.create_group()
        return jsonify(
        {
            "status": 201, 
            "message": "You have successfully created a new group",
            "data": create
            }
        ), 201

@groups_blueprint.route('/groups/<int:id>', methods=['DELETE'])
@jwt_required
@swag_from('../apidocs/delete_group.yml', methods=['DELETE'])
def delete_a_group(id):
    current_user=get_jwt_identity()
    createdby=current_user['user_id']
    delete = Group.delete_group(id, createdby)
    if delete:
        return jsonify({
            "status":200,
            "message":"You have successfully deleted your group"
        })
    return jsonify({
        "status":400,
        "message":"Either you do not own that group or it does not exist"
    }),400

@groups_blueprint.route('/groups/users/members', methods=['POST'])
@jwt_required
@swag_from('../apidocs/add_user_to_group.yml', methods=['POST'])
def add_user_group():
    current_user=get_jwt_identity()

    data=request.get_json(force=True)
    group_name=data['group_name']
    member=data['member']
    if not User.get_user_by_email(member):
        return jsonify(
            {
                "status": 404,
                "message": "The user you are trying to add does not exist in the system"
            }
        )
    if not Group.check_groupname_existance(group_name):
        return jsonify({
            "status":404,
            "message": "The group does not exist yet"
        }),404
    if Group.get_member_from_group(member, group_name):
        return jsonify({
            "status": 409,
            "message": "The member you are trying to add into the group already exists"
        }),409

    if not Group.get_groups(current_user['email']):
        return jsonify({
            "status": 401,
            "message": "You can not add a member to a group you did not create"
        })

    new_member=Group.add_member(group_name,member)
    if new_member:
        return jsonify({
            "status":201,
            "message":"You have added a new member to the group"
        }),201
    return jsonify({
        "status":203,
        "message":"We were not able to add a user to your group"
    }),203

@groups_blueprint.route('/groups/<int:group_id>/users/<int:user_id>', methods=['DELETE'])
@jwt_required
@swag_from('../apidocs/delete_group_user.yml', methods=['DELETE'])
def delete_user_from_group(group_id, user_id):
    deleted=Group.delete_user(group_id, user_id)
    if deleted:
        return jsonify({
            "status":200,
            "message":"You have deleted a member from your group successfully"
        }),200
    return jsonify({
            "status":404,
            "message":"User specified was not found"
        })

@groups_blueprint.route('/groups/messages', methods=['POST'])
@jwt_required
@swag_from('../apidocs/create_group_mail.yml', methods=['POST'])
def create_group_mail():
    data=request.get_json(force=True)
    current_user=get_jwt_identity()
    email=current_user['email']
    data=request.get_json()
    group_name=data['group_name']
    subject=data['subject']
    message=data['message']
    status=data['status']
    createdby=email

    if validate_subject(subject):
        return validate_subject
    if validate_message(message):
        return validate_message
    Group.create_group_message(group_name,subject,message,status,createdby)
    return jsonify({
        "status":201,
        "message":"Group messages successfully created."
    }),201

@groups_blueprint.route('groups/all', methods=['GET'])
@jwt_required
def get_all_groups():
    """Gets all groups a user has """
    current_user=get_jwt_identity()
    group_owner=current_user['email']
    get_groups=Group.get_groups(group_owner)
    if get_groups:
        return jsonify({
            "status":200,
            "data": get_groups
        }),200
    return jsonify({
        "status":404,
        "message":"You have not created any groups yet"
    })
    
@groups_blueprint.route('groups/members/<string:name>', methods=['GET'])
@jwt_required
def get_all_members(name):
    # result=Group.get_all_members_in_group(name)
    # if result:
    return jsonify({
        "status":200,
        "data": Group.get_all_members_in_group(name)
    })
    # return jsonify({
    #     "status":404,
    #     "message": "Feels like there are no members in this group"
    # })