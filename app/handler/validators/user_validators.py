import re
from flask import jsonify

def validate_firstname(firstname):
    """Validation for the field of first name in the User model"""
    if not firstname:
        error = {
            "status": 400,
            "message":"You must provide the first name field"
        }
        return jsonify(error), 400
    elif len(str(firstname)) < 5:
        error = {
            "status": 400,
            "message":"Names accepted must be at least 5 characters"
        }
        return jsonify(error), 400
    elif not isinstance(firstname, str):
        error = {
            "status": 400,
            "message":"The name must be a string"
        }
        return jsonify(error), 400
    elif re.search("[0-9]", str(firstname)) or re.search("[$#@*&%!~`+=|':;.><,_-]", str(firstname)):
        error = {
            "status": 400,
            "message":"Do not use special characters and numbers on a name"
        }
        return jsonify(error), 400



def validate_lastname(lastname):
    """Validation for the field of last name in the User model"""
    if not lastname:
        error = {
            "status": 400,
            "message":"You must provide the last name field"
        }
        return jsonify(error), 400
    elif len(str(lastname)) < 5:
        error = {
            "status": 400,
            "message":"Names accepted must be at least 5 characters"
        }
        return jsonify(error), 400
    elif not isinstance(lastname, str):
        error = {
            "status": 400,
            "message":"The name must be a string"
        }
        return jsonify(error), 400
    elif re.search("[0-9]", str(lastname)) or re.search("[$#@*&%!~`+=|':;.><,_-]", str(lastname)):
        error = {
            "status": 400,
            "message":"Do not use special characters and numbers on a name"
        }
        return jsonify(error), 400


def validate_password(password):
    if len(password) < 4:
        error = {
            "status": 400,
            "message":"Your password must have 5 characters and above"
        }
        return jsonify(error)
    elif re.search('[0-9]',password) is None:
        error = {
            "status": 400,
            "message":"Your password must at least a number in it"
        }
        return jsonify(error)
    elif re.search('[A-Z]',password) is None:
        error = {
            "status": 400,
            "message":"Your password must at least contain an uppercase character"
        }
        return jsonify(error)
    elif re.search("[$#@*&%!~`+=|':;.><,_-]",password) is None:
        error = {
            "status": 400,
            "message":"Your password must at least a special character"
        }
        return jsonify(error)


def validate_email(email):
        """
        validates email
        """
        if not email or email.isspace():
            return jsonify({
                "status": 400,
                "message": "Fill in the email"
            })
        valid_email = re.compile(
            r"(^[a-zA-Z0-9_.]+@[a-zA-Z0-9]+\.[a-z]+$)")
        if not valid_email.match(email):
            return jsonify({
                "status": 400,
                "message": "please input valid email"
            })
    
        return None
