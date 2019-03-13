from flask import url_for, request, Blueprint, jsonify
from flask_bcrypt import generate_password_hash
from app.users.model import User, users

user_bp = Blueprint('user', __name__)


# user signup
@user_bp.route('/signup', methods=['POST', 'GET'])
def signup():
    if request.method == "POST":
        data =request.get_json()

        id=len(users)+1
        firstname = data['firstname']
        lastname = data['lastname']
        email = data['email']
        password_hash = data['password_hash']
        new_user = User(
            id=id,
            firstname=firstname,
            lastname=lastname,
            email=email,
            password_hash=password_hash
        )
        users.append(new_user.to_dictionary())
        return jsonify(
            {
                "status": 201, 
                "message":"You have successfully created an account", 
                "data":new_user.to_dictionary()
            }
        ), 201

