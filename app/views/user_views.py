import datetime
from flask import Blueprint, request, make_response, jsonify
from app import bcrypt, swag
from app.models.users import User
from app.handler.validators.user_validators import (
    validate_firstname, validate_lastname, validate_email, validate_password
)
from app.models.db import DatabaseConnection
from flask_jwt_extended import create_access_token
from flasgger import swag_from


user_blueprint = Blueprint('user', __name__)


@user_blueprint.route('/auth/signup', methods=['POST'])   
@swag_from('../apidocs/signup.yml', methods=['POST'])
def signup_user():
    data = request.get_json()    
    user = User(
            firstname=data['firstname'],
            lastname = data['lastname'],
            email = data['email'],
            password =data['password']
            )
    email_check = User.get_user_by_email(user.email)
    if email_check:
        return jsonify({
            "status":409,
            "message":"User already exists"
        }),409
    if validate_email(user.email):
        return validate_email(user.email)
    if validate_firstname(user.firstname):
        return validate_firstname(user.firstname)
    if validate_lastname(user.lastname):
        return validate_lastname(user.lastname)
    if validate_password(user.password):
            return validate_password(user.password)
    new_user = user.create_user()
    return jsonify(
        {
            "status": 201, 
            "message": "You have successfully created an account",
            "data": new_user
            }
        ), 201

@user_blueprint.route('/auth/login', methods=['POST'])
@swag_from('../apidocs/login.yml', methods=['POST'])
def login_user():
    data = request.get_json()
    email=data['email']
    password=data['password']
    
    check_email= User.get_user_by_email(email)
    if not check_email:
        return jsonify({
            "status": 404,
            "message": "Email was not found in the system."
        })
    log_in=User.login_user(email, password)
    if log_in:
        user_id = User.get_user_id(email)
        if user_id:
            access_token =create_access_token(identity=user_id)
        return jsonify({
            "status": 200,
            "message": "You are logged in successfully",
            "data": log_in['email'],
            "token": access_token
        }),200