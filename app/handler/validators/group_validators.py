import re
from flask import jsonify
from app.models.group_model import Group

def check_group_id(id):
    check_existance=Group.check_group_by_id(id)
    if not check_existance:
        error={
            "status": 404,
            "message": "Group id does not match any groups"
        }
    elif not id:
        error={
            "status":400,
            "message":"Group id field can not be left empty"
        }
    elif not id <=0:
        error={
            "status":400,
            "message":"Group id field can not a zero or below"
        }
    elif not isinstance(id, int):
        error={
            "status":400,
            "message":"Group id should be an integer"
        }
    return jsonify(error),400