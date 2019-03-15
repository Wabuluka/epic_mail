# epicmail/app/handlers/validators.py
from flask import jsonify, request


class Validations:

    def validate_content_type(self, contentType):
       if contentType != "application/json":
            return {
                "status": 400,
                "error": "Wrong content Type"
            }