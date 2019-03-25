from flask import Blueprint, request, make_response, jsonify
from app.models.messages import Message
from app.handler.validators.message_validators import (
    validate_address, validate_createdby, validate_message, validate_subject)

# blueprint for the message
messages_blueprint = Blueprint('messages', __name__)


@messages_blueprint.route('/messages', methods=['POST'])   
def post(self):
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
        if validate_createdby(createdby):
            return validate_createdby
        if validate_address(address):
            return validate_address
        
        data = Message(subject, message, status, createdby, address)
        msg = data.create_message(subject, message, status, createdby, address)
        return jsonify(msg), 201


@messages_blueprint.route('/messages/<int:id>', methods=['GET'])    
def get_one_message(self, id):
    """Get a message by id"""
    return jsonify(Message.find_message_by_id(id))

@messages_blueprint.route('/messages', methods=['GET'])    
def get_all_messages(self):
    """User fetches all the mails"""
    return jsonify(Message.get_all_messages())
        
@messages_blueprint.route('/message/<int:id>', methods=['DELETE'])   
def delete_message(self, id):
    """Delete a mail by a user"""
    return jsonify(Message.delete_message(id)),200

@messages_blueprint.route('/messages/update/<int:id>', methods=['PATCH'])
def update_status(self, id):
    data = request.get_json()
    status = data['status']
    return jsonify(Message.update_status(id, status))

@messages_blueprint.route('/messages/received', methods=['GET'] )
def get_all_received_messages(self):
    return jsonify(Message.get_all_received_messages()),200

@messages_blueprint.route('/messages/sent', methods=['GET'])
def get(self):
    return jsonify(Message.get_all_sent_messages()),200
