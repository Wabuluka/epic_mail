import datetime
from flask import Blueprint, request, make_response, jsonify
from app import bcrypt
from app.models.users import User
from app.handler.validators.user_validators import (
    validate_firstname, validate_lastname, validate_email, validate_password
)
from app.models.db import DatabaseConnection

usermodel = User()

user_blueprint = Blueprint('user', __name__)


@user_blueprint.route('/auth/signup', methods=['POST'])   
def signup_user():
    """Method View for creating new accounts"""
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

@user_blueprint.route('/auth/login', methods=['POST']) 
def post(self):
    """Users with accounts can log in"""
    data = request.get_json()
    email = data.get("email", None)
    password = data.get("password", None)
    return jsonify(User.login_user(email, password))    
