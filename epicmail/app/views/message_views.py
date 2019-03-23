from flask import Blueprint, request, make_response, jsonify
from flask.views import MethodView
from epicmail.app.views.user_views import LoginUser
from epicmail.app.models.messages import Message
from epicmail.app.handler.validators.message_validators import (
    validate_address, validate_createdby, validate_message, validate_subject)

# blueprint for the message
messages_blueprint = Blueprint('messages', __name__)

class SendMessage(MethodView):
    """Method View for creating a new email"""
    def post(self):
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


class GetSpecificMail(MethodView):
    """Get a message as specified by the user"""
    def get(self, id):
        """Get a message by id"""
        return jsonify(Message.find_message_by_id(id))


class GetAllMail(MethodView):
    """User fetches all the mails"""
    def get(self):
        return jsonify(Message.get_all_messages())
        

class DeleteMail(MethodView):
    """Delete a mail by a user"""
    def delete(self, id):
        return jsonify(Message.delete_message(id)),200


class UpdateStatus(MethodView):
    def patch(self, id):
        data = request.get_json()
        status = data['status']
        return jsonify(Message.update_status(id, status))

class GetReceivedMessages(MethodView):
    def get(self):
        return jsonify(Message.get_all_received_messages()),200


class GetAllSentMessages(MethodView):
    def get(self):
        return jsonify(Message.get_all_sent_messages()),200

        


send_message = SendMessage.as_view('create_message')
get_message = GetSpecificMail.as_view('get_message')
get_messages = GetAllMail.as_view('get_messages')
delete_message = DeleteMail.as_view('del_message')
update_status = UpdateStatus.as_view('update_statuses')
get_received = GetReceivedMessages.as_view('get_received')
get_sent = GetAllSentMessages.as_view('get_sent')


messages_blueprint.add_url_rule(
    '/messages',
    view_func=send_message,
    methods=['POST']
)
messages_blueprint.add_url_rule(
    '/messages/<int:id>',
    view_func=get_message,
    methods=['GET']
)
messages_blueprint.add_url_rule(
    '/messages',
    view_func=get_messages,
    methods=['GET']
)
messages_blueprint.add_url_rule(
    '/messages/<int:id>',
    view_func=delete_message,
    methods=['DELETE']
)
messages_blueprint.add_url_rule(
    '/messages/update/<int:id>',
    view_func=update_status,
    methods=['PATCH']
)
messages_blueprint.add_url_rule(
    '/messages/received',
    view_func=get_received,
    methods=['GET']
)
messages_blueprint.add_url_rule(
    '/messages/sent',
    view_func=get_sent,
    methods=['GET']
)