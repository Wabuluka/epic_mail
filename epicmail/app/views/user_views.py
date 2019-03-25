import datetime
from flask import Blueprint, request, make_response, jsonify
from epicmail.app import bcrypt
from flask.views import MethodView
from epicmail.app.models.users import User
from epicmail.app.handler.validators.user_validators import (
    validate_firstname, validate_lastname, validate_email, validate_password
)
from epicmail.app.models.db import DatabaseConnection

usermodel = User()

user_blueprint = Blueprint('user', __name__)

class RegisterUser(MethodView):
    """Method View for creating new accounts"""
    def post(self):
        data = request.get_json()
        email = data['email']
        firstname = data['firstname']
        lastname = data['lastname']
        password =data['password']
        registered_on = datetime.datetime.utcnow()
        
        user = User(firstname=firstname,lastname=lastname,email=email,password=password,registered_on=registered_on)
        usermodel.create_user(user)
        return jsonify({
            "status":201,
            "message": "You have successfully created an account."
        })

class LoginUser(MethodView):
    """Users with accounts can log in"""
    def post(self):
        data = request.get_json()
        email = data.get("email", None)
        password = data.get("password", None)
        return jsonify(User.login_user(email, password))    

registration_view = RegisterUser.as_view('register_user')
login_view = LoginUser.as_view('login_user')

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