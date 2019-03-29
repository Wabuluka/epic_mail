import datetime
from flask import Blueprint, request, make_response, jsonify
from app.models.group_model import Group
from app.models.db import DatabaseConnection
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.handler.validators.message_validators import validate_message, validate_subject
from app.handler.validators.group_validators import check_group_id


groups_blueprint = Blueprint('groups', __name__)


@groups_blueprint.route('/groups', methods=['POST'])
@jwt_required
def create_new_group():
    data_posted = request.get_json()
    if request.method == "POST":
        new_group=Group(
            group_name=data_posted['group_name'],
            role=data_posted['role'],
            createdby=data_posted['createdby']
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

@groups_blueprint.route('/groups/<int:id>/users', methods=['POST'])
@jwt_required
def add_user_group(id):
    data=request.get_json()
    group_id=data['group_id']
    member=data['member']
    new_member=Group.add_member(group_id,member)
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

@groups_blueprint.route('/groups/<int:group_id>/messages', methods=['POST'])
@jwt_required
def create_group_mail(group_id):
    current_user=get_jwt_identity()
    user_id=current_user['user_id']
    data=request.get_json()
    group_id=group_id
    subject=data['subject']
    message=data['message']
    status=data['status']
    createdby=user_id

    if check_group_id(group_id):
        return check_group_id
    if validate_subject(subject):
        return validate_subject
    if validate_message(message):
        return validate_message
    Group.create_group_message(group_id,subject,message,status,createdby)
    return jsonify({
        "status":201,
        "message":"Group messages successfully created."
    }),201
