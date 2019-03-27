import datetime
from flask import Blueprint, request, make_response, jsonify
from app.models.group_model import Group
from app.models.db import DatabaseConnection


groups_blueprint = Blueprint('groups', __name__)


@groups_blueprint.route('/groups', methods=['POST'])
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

@groups_blueprint.route('//groups/<int:id>', methods=['DELETE'])
def delete_a_group(id):
    pass