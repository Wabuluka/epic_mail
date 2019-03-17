# epicmail/app/users/views.py

from flask import Blueprint, request, make_response, jsonify
from epicmail.app import bcrypt
from flask.views import MethodView
from epicmail.app.models.users import User, users

user_blueprint = Blueprint('user', __name__)

class RegisterUser(MethodView):
    """Method View for creating new accounts"""
    def post(self):
        # get data from json
        data_posted = request.get_json()
        # check for user existence
        for user in (users):
            if user['email'] == data_posted['email']:
                responseObject = {
                    'status': 202,
                    'message': 'User with that email already exists, please try with another email'
                }
                return make_response(jsonify(responseObject)), 202
            
        if request.method == "POST":
            user_id=len(users)+1
            firstname = data_posted['firstname']
            lastname = data_posted['lastname']
            email = data_posted['email']
            password = data_posted['password']

            # validating the necessary fields
            val_firstname = User.validate_firstname(firstname)
            val_lastname = User.validate_lastname(lastname)
            val_password = User.validate_password(password)
            val_email = User.validate_email(email)
            if val_firstname:
                return val_firstname
            elif val_lastname:
                return val_lastname
            elif val_password:
                return val_password
            elif val_email:
                return val_email
            # create a new user instance
            new_user = User(
                user_id=user_id,
                firstname=firstname,
                lastname=lastname,
                email=email,
                password=password
            )
            users.append(new_user.to_dictionary())
            auth_token = new_user.encode_auth_token(new_user.user_id) 
            responseObject = {
                "status": 201,
                "message": "You have successfully created an account",
                "data":[
                    {
                        "token": str(auth_token.decode()),
                        "data": new_user.to_dictionary()
                    }
                ]
            }
            return make_response(jsonify(responseObject)), 201
        else:
            responseObject = {
                "status": '401',
                "message": "You were unable to create an account, please try again!"
            }
            return make_response(jsonify(responseObject)), 401

class LoginUser(MethodView):
    """Users with accounts can log in"""
    def post(self):
        # login the user
        data_posted = request.get_json(force=True)
        email = data_posted['email']
        password = data_posted['password'] 
        for l_user in users:
            if l_user['email'] == email and bcrypt.check_password_hash(l_user['password'], password):
                
                user_logged_in = l_user
                # auth_token = l_user.encode_auth_token(l_user.user_id)
                responseObject = {
                    'status': 200,
                    'message': 'Successfully logged in.',
                    # 'token': auth_token,
                    'user':user_logged_in,
                }
                return make_response(jsonify(responseObject)), 200

        responseObject = {
                'status': 401,
                'message':'Unathorized, either email or password is incorrect'
            }
        return make_response(jsonify(responseObject)), 401  

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
                