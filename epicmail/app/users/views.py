# epicmail/app/users/views.py

from flask import Blueprint, request, make_response, jsonify
from flask.views import MethodView
from epicmail.app.models import User, users


user_blueprint = Blueprint('user', __name__)

class RegisterUser(MethodView):

    """Method View for creating new accounts"""

    def post(self):
        # get data from json
        data_posted = request.get_json()

        if request.method == "POST":
            user_id=len(users)+1
            firstname = data_posted['firstname']
            lastname = data_posted['lastname']
            email = data_posted['email']
            password_hash = data_posted['password_hash']

            # create a new user instance
            new_user = User(
                user_id=user_id,
                firstname=firstname,
                lastname=lastname,
                email=email,
                password_hash=password_hash
            )
            users.append(new_user.to_dictionary())
            auth_token = new_user.encode_auth_token(new_user.user_id)
            responseObject = {
                "status": '201',
                "message": "You have successfully created an account",
                "token": auth_token.decode(),
                "data": new_user.to_dictionary()
            }
            return make_response(jsonify(responseObject)), 201
        else:
            responseObject = {
                "status": '401',
                "message": "You were unable to create an account, please try again!"
            }
            return make_response(jsonify(responseObject)), 401

# define the API resources
registration_view = RegisterUser.as_view('user_blueprint')

# add Rules for API Endpoints
user_blueprint.add_url_rule(
    '/auth/signup',
    view_func=registration_view,
    methods=['POST']
)
                