from flask import Blueprint, request, make_response, jsonify
from app.models.messages import Message
from app.models.users import User
from app.handler.validators.message_validators import (validate_createdby, validate_message, validate_subject)
from app import jwt
from flask_jwt_extended import jwt_required, get_jwt_identity
from flasgger import swag_from


messages_blueprint = Blueprint('messages', __name__)


@messages_blueprint.route('/messages', methods=['POST'])
@jwt_required
@swag_from('../apidocs/create_message.yml', methods=['POST'])
def create_msg():
    """Method View for creating a new email"""
    data_posted = request.get_json(force=True)
    current_user = get_jwt_identity()
    if request.method == "POST":
        new_message=Message(
            subject=data_posted['subject'],
            message=data_posted['message'],
            status=data_posted['status'],
            createdby=current_user['email'],
            address=data_posted['address'],
            parentMessageId=0
        )
        if not User.get_user_by_email(new_message.address):
            return jsonify({
                "status":404,
                "message":"The person you are sending the email to does not exist"
            })
        if validate_subject(new_message.subject):
            return validate_subject
        if validate_message(new_message.message):
            return validate_message

        # data = Message(subject, message, status, createdby, address, parentMessageId)
        msg = new_message.create_message()
        return jsonify(
            {
                "status": 201,
                "message": "Message has been created successfully",
                "data": msg
            }
        )

@messages_blueprint.route('/messages/<int:id>', methods=['GET'])
@jwt_required
@swag_from('../apidocs/get_mail.yml', methods=['GET'])
def get_one_message(id):
    """Get a message by id"""
    current_user=get_jwt_identity()
    current_user=current_user['email']
    result=Message.find_message_by_id(id,current_user)
    if result:
        return jsonify({
            "status":200,
            "data": result
        }),200
    return jsonify({
        "status":404,
        "message":"Mail not found"
    })

@messages_blueprint.route('/messages', methods=['GET'])
@jwt_required
@swag_from('../apidocs/get_mails.yml', methods=['GET'])
def get_all_messages():
    """User fetches all the mails"""
    return jsonify(Message.get_all_messages())

@messages_blueprint.route('/messages/<int:id>', methods=['DELETE'])
@jwt_required
@swag_from('../apidocs/delete_mail.yml', methods=['DELETE'])
def delete_message(id):
    """Delete a mail by a user"""
    current_user=get_jwt_identity()
    address=current_user['email']
    deleted=Message.delete_message(id, address)
    if deleted:
        return jsonify(
            {
                "status":200,
                "message":"Message has been successfully deleted"
            }
        )
    return jsonify(
            {
                "status":404,
                "message":"Message was not found"
            }
        )

@messages_blueprint.route('/messages/update/<int:id>', methods=['PATCH'])
@jwt_required
# @swag_from('../apidocs/edit_status.yml', methods=['PATCH'])
def update_status(id):
    data = request.get_json()
    table_name = 'messages'
    status = data['status']
    Message.update_status(table_name, status, id)
    return jsonify(
            {
                "status": 200,
                "message": "status updated successfully"
            }
        )

@messages_blueprint.route('/messages/unread', methods=['GET'])
@jwt_required
@swag_from('../apidocs/message_unread.yml', methods=['GET'])
def get_unread_messages():
    current_user = get_jwt_identity()
    email= current_user['email']
    unread_messages=Message.get_unread_messages(email)
    if unread_messages:
        return jsonify(
            {
                "status":200,
                "data": unread_messages
            }
        ),200
    return jsonify(
            {
                "status":404,
                "data": "Unread messages were not found"
            }
        ),404

@messages_blueprint.route('/messages/sent', methods=['GET'])
@jwt_required
# @swag_from('../apidocs/message_sent.yml', methods=['GET'])
def get_all_messages_sent():
    current_user=get_jwt_identity()
    email=current_user['email']
    msg=Message.get_all_messages_sent_by_a_user(email)
    if msg:
        return jsonify({
                "status":200,
                "data":msg
            }),200
    return jsonify({
        "status":404,
        "message": "You have not sent any emails yet"
    })

@messages_blueprint.route('/messages/received', methods=['GET'])
@jwt_required
# @swag_from('../apidocs/get_received_mail.yml', methods=['GET'])
def get_received():
    current_user=get_jwt_identity()
    address=current_user['email']
    if address:
        msg=Message.get_received_messages(address)
        return jsonify({
            "status":200,
            "data":msg
        })
    return jsonify({
        "status":404,
        "message": "You have not received any messages yet"
    })
