# epicmail/app/messages/views.py

from flask import Blueprint, request, make_response, jsonify
from flask.views import MethodView
from epicmail.app.users.views import LoginUser
from epicmail.app.models.messages import Messages, messages

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
                "message": "Your message has been successfully  sent"
            }
            return make_response(jsonify(responseObject)), 201

# define the Messages rources
send_message = SendMessage.as_view('create_message')

# add Rules for Endpoints
messages_blueprint.add_url_rule(
    '/messages',
    view_func=send_message,
    methods=['POST']
)