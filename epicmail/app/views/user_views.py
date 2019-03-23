# epicmail/app/users/views.py

from flask import Blueprint, request, make_response, jsonify
from epicmail.app import bcrypt
from flask.views import MethodView
from epicmail.app.models.users import User
from epicmail.app.handler.auth import JwtAuth
from epicmail.app.handler.validators.user_validators import (
    validate_firstname, validate_lastname, validate_email, validate_password
)
authentic = JwtAuth()
user_blueprint = Blueprint('user', __name__)

class RegisterUser(MethodView):
    """Method View for creating new accounts"""
    def post(self):
        # get data from json
        data = request.get_json()
        # check for user existence
        email = data['email']
        firstname = data['firstname']
        lastname = data['lastname']
        password =data['password']
        
        if validate_email(email):
            return validate_email(email)
        if validate_firstname(firstname):
            return validate_firstname(firstname)
        if validate_lastname(lastname):
            return validate_lastname(lastname)
        if validate_password(password):
            return validate_password(password)
        
        user = User(email, firstname, lastname, password)
        data2=user.create_user(email, firstname, lastname, password)
        return jsonify(data2),201

class LoginUser(MethodView):
    """Users with accounts can log in"""
    def post(self):
        data = request.get_json()
        email = data.get("email", None)
        password = data.get("password", None)
        return jsonify(User.login_user(email, password))    

# define the API resources
registration_view = RegisterUser.as_view('register_user')
login_view = LoginUser.as_view('login_user')

# add Rules for API Endpoints
user_blueprint.add_url_rule(
    '/auth/signup',
    view_func=registration_view,
    methods=['POST']
)
user_blueprint.add_url_rule(
    '/auth/login',
    view_func=login_view,
    methods=['POST']
)