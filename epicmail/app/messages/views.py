# epicmail/app/messages/views.py

from flask import Blueprint, request, make_response, jsonify
from flask.views import MethodView
from epicmail.app.users.views import LoginUser
from epicmail.app.models.messages import Messages, messages

# blueprint for the message
messages_blueprint = Blueprint('messages', __name__)


class SendMessage(MethodView):
    """Method View for creating a new email"""
    def post(self):
        # get data from json
        data_posted = request.get_json()
        if request.method == "POST":
            subject=data_posted['subject']
            message=data_posted['message']
            status=data_posted['status']
            createdby=data_posted['createdby']
            address=data_posted['address']
            # in refernce to the model
            new_message = Messages(
                subject=subject,
                message=message,
                status=status,
                createdby=createdby,
                address=address
            )
            messages.append(new_message.to_dictionary())
            responseObject = {
                "status": 201,
                "message": "Your message has been successfully sent.",
                "data": new_message.to_dictionary()
            }
            return make_response(jsonify(responseObject)), 201


class GetSpecificMail(MethodView):
    """Get a message as specified by the user"""
    def get(self, id):
        """Get a message by id"""
        for message in messages:
            if message['id'] == id:
                responseObject = {
                    'status': 200,
                    'message': message
                }
                return make_response(jsonify(responseObject)), 200
        responseObject = {
                'status': 401,
                'message':'Unathorized, either email or password is incorrect'
            }
        return make_response(jsonify(responseObject)), 401


class GetAllMail(MethodView):
    """User fetches all the mails"""
    def get(self):
        if messages == []:
            responseObject = {
                'statu': 404,
                'message': 'There were no messages found.'
            }
            return make_response(jsonify(responseObject)), 404
        responseObject = {
            'status': 200,
            'data': messages
        }
        return make_response(jsonify(responseObject)),200

class DeleteMail(MethodView):
    """Delete a mail by a user"""
    def delete(self, id):
        if len(messages) < 1:
            responseObject = {
                'status': 404,
                'message': 'No messages were found'
            }
            return make_response(jsonify(responseObject)), 404
        for message in messages:
            if messages[message]["id"] == id:
                del messages[message]
                responseObject = {
                    'status': 200,
                    'message': [{"id":id}]
                }
                return make_response(jsonify(responseObject)), 200
        responseObject = {
           'status': 404,
            'message': 'No message was found' 
        }
        return make_response(jsonify(responseObject)), 404



# define the Messages rources
send_message = SendMessage.as_view('create_message')
get_message = GetSpecificMail.as_view('get_message')
get_messages = GetAllMail.as_view('get_messages')
delete_message = DeleteMail.as_view('del_message')

# add Rules for Endpoints
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