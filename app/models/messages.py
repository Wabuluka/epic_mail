import datetime
from flask import jsonify
import re



class Message:
    """Messages Models contains properties stored for a message to be sent to an individual"""
    messages_list = []

    def __init__(self, subject, message, status, createdby, address):
        """Initializes the message"""
        self.id=len(Message.messages_list)+1
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

    def create_message(self,subject, message, status, createdby, address):
        message = Message(subject, message, status, createdby, address)
        Message.messages_list.append(message.to_dictionary())
        return {
            "status": 201,
            "message": "Message has been created successfully",
            "data": message.to_dictionary()
        }

    @staticmethod
    def find_message_by_id(id):
        for message in Message.messages_list:
            if id == message['id']:
                return message

    @staticmethod
    def delete_message(id):
        message = Message.find_message_by_id(id)
        for message in Message.messages_list:
            if message:
                Message.messages_list.remove(message)
                return {
                    "status": 200,
                    "message": "You have successfully deleted the message"
                }
        return {
            "status": 404,
            "message":"Message with that id was not found"
        }    

    @staticmethod
    def update_status(id, stats):
        message = Message.find_message_by_id(id)
        for message in Message.messages_list:
            if message:
                message.update(status = stats)
                return {
                    "status": 200,
                    "message": "You have successfully updated",
                    "data": message
                }
        return {
            "status": 404,
            "message": "The message was not found."
            }

    @staticmethod
    def get_all_messages():
        if Message.messages_list:
            return {
                "status": 200,
                "data": Message.messages_list
            }
        return {
            "status": 404,
            "message": "No messages were found."
        }

    @staticmethod
    def get_all_received_messages():
        for message in Message.messages_list:
            if message['status'] == 'read' or message['status'] == 'sent':
                return {
                    "status": 200,
                    "data": message
                }
        return {
            "status": 404,
            "message": "There are no messages yet"
        }
    
    @staticmethod
    def get_all_sent_messages():
        for message in Message.messages_list:
            if message['status'] == 'sent':
                return {
                    "status": 200,
                    "data": message
                }
        return {
            "status": 404,
            "message": "There are no messages sent yet"
        }