import re
from flask import jsonify

def validate_subject(subject):
    if not subject:
        error = {
            "status": 401,
            "error":"You must fill the subject field."
        }
        return jsonify(error), 401


def validate_message(message):
    if not message:
        error = {
            "status": 401,
            "error":"You must fill the message field."
        }
        return jsonify(error), 401

def validate_address(address):
    if not address:
        error = {
            "status": 401,
            "error":"You must fill the address field."
        }
        return jsonify(error), 401
    address = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', address)
    if address  == None:
        error = {
            'status':401,
            'error': 'Make sure your address is well written.'
        }
        return jsonify(error)


def validate_createdby(createdby):
    if not createdby:
        error = {
            "status": 401,
            "error":"You must fill the createdby field."
        }
        return jsonify(error), 401
    createdby = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', createdby)
    if createdby  == None:
        error = {
            'status':401,
            'error': 'Make sure your createdby is well written.'
        }
        return jsonify(error)