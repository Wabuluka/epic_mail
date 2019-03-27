from flask import Blueprint, request, make_response, jsonify
from app.models.messages import Message
from app.handler.validators.message_validators import (
    validate_address, validate_createdby, validate_message, validate_subject)
from app import jwt
from flask_jwt_extended import jwt_required, get_jwt_identity


# blueprint for the message
messages_blueprint = Blueprint('messages', __name__)


@messages_blueprint.route('/messages', methods=['POST'])   
@jwt_required
def create_msg():
    """Method View for creating a new email"""
    data_posted = request.get_json()
    if request.method == "POST":
        current_user = get_jwt_identity()
        subject=data_posted['subject']
        message=data_posted['message']
        status=data_posted['status']
        createdby=current_user['user_id']
        address=data_posted['address']
        parentMessageId=0

        if validate_subject(subject):
            return validate_subject
        if validate_message(message):
            return validate_message
        if validate_address(address):
            return validate_address
        
        data = Message(subject, message, status, createdby, address, parentMessageId)
        msg = data.create_message()
        # print(current_user['user_id'])
        return jsonify(
            {
                "status": 201,
                "message": "Message has been created successfully",
                "data": msg
            }
        )


@messages_blueprint.route('/messages/<int:id>', methods=['GET'])  
@jwt_required  
def get_one_message(id):
    """Get a message by id"""
    return jsonify(Message.find_message_by_id(id))

@messages_blueprint.route('/messages', methods=['GET']) 
@jwt_required   
def get_all_messages():
    """User fetches all the mails"""
    return jsonify(Message.get_all_messages())
        
@messages_blueprint.route('/messages/<int:id>', methods=['DELETE'])   
@jwt_required
def delete_message(id):
    """Delete a mail by a user"""
    return jsonify(Message.delete_message(id))

@messages_blueprint.route('/messages/update/<int:id>', methods=['PATCH'])
@jwt_required
def update_status(id):
    data = request.get_json()
    table_name = 'messages'
    status = data['status']
    Message.update_status(table_name, status, id)
    return jsonify(
        {
            "status": 200
        }
    )

@messages_blueprint.route('/messages/unread', methods=['GET'])
@jwt_required
def get_unread_messages():
    current_user = get_jwt_identity()
    id= current_user['user_id']
    print(id)
    return jsonify(Message.get_unread_messages(id))

@messages_blueprint.route('/messages/sent', methods=['GET'])
@jwt_required
def get_all_messages_sent():
    current_user=get_jwt_identity()
    id=current_user['user_id']
    return jsonify(Message.get_all_messages_sent_by_a_user(id))
