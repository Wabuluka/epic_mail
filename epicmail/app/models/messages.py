# empicmail/app/models/messages.py
import datetime

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
            "createdby":self.createdby,
            "createdon":self.createdon,
            "message":self.message,
            "status":self.status,
            "address":self.address
        }


class MessageReply(Messages):
    """MessageReply Models contains properties stored for a message to be replied to an individual"""
    def __init__(self, createdon, Message_repy, parent_message_id, reply_status):
        """Initializes the message reply"""
        pass