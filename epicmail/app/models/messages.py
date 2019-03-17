# empicmail/app/models/messages.py
import datetime
from flask import jsonify
import re

messages = []

class Messages:
    """Messages Models contains properties stored for a message to be sent to an individual"""
    def __init__(self, subject, message, status, createdby, address):
        """Initializes the message"""
        self.id=len(messages)+1
        self.createdon=datetime.datetime.now()
        self.subject=subject
        self.message=message
        self.status=status
        self.createdby=createdby
        self.address=address

    def to_dictionary(self):
        return {
            "id":self.id,
            "subject":self.subject,
            "createdby":self.createdby,
            "createdon":self.createdon,
            "message":self.message,
            "status":self.status,
            "address":self.address
        }

    @staticmethod
    def validate_subject(subject):
        if not subject:
            error = {
                "status": 401,
                "error":"You must fill the subject field."
            }
            return jsonify(error), 401
    
    @staticmethod
    def validate_message(message):
        if not message:
            error = {
                "status": 401,
                "error":"You must fill the message field."
            }
            return jsonify(error), 401
    @staticmethod
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
    
    @staticmethod
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

class MessageReply(Messages):
    """MessageReply Models contains properties stored for a message to be replied to an individual"""
    def __init__(self, createdon, Message_repy, parent_message_id, reply_status):
        """Initializes the message reply"""
        pass