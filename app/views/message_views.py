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
        subject=data_posted['subject']
        message=data_posted['message']
        status=data_posted['status']
        createdby=data_posted['createdby']
        address=data_posted['address']

        if validate_subject(subject):
            return validate_subject
        if validate_message(message):
            return validate_message
        if validate_address(address):
            return validate_address
        
        data = Message(subject, message, status, createdby, address)
        msg = data.create_message()
        current_user = get_jwt_identity()
        print(current_user['user_id'])
        return jsonify(
            {
                "status": 201,
                "message": "Message has been created successfully",
                "data": msg
            }
        )


@messages_blueprint.route('/messages/<int:id>', methods=['GET'])    
def get_one_message(id):
    """Get a message by id"""
    return jsonify(Message.find_message_by_id(id))

@messages_blueprint.route('/messages', methods=['GET'])    
def get_all_messages():
    """User fetches all the mails"""
    return jsonify(Message.get_all_messages())
        
@messages_blueprint.route('/messages/<int:id>', methods=['DELETE'])   
def delete_message(id):
    """Delete a mail by a user"""
    return jsonify(Message.delete_message(id))

@messages_blueprint.route('/messages/update/<int:id>', methods=['PATCH'])
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
# @messages_blueprint.route('/messages/received', methods=['GET'] )
# def get_all_received_messages(self):
#     return jsonify(Message.get_all_received_messages()),200

# @messages_blueprint.route('/messages/sent', methods=['GET'])
# def get(self):
#     return jsonify(Message.get_all_sent_messages()),200
