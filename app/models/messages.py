import datetime
from flask import jsonify
import re
from app.models.db import DatabaseConnection


database=DatabaseConnection()
cur=database.cursor
database.create_messages_table()


class Message:
    """Messages Models contains properties stored for a message to be sent to an individual"""

    def __init__(self, subject, message, status, createdby, address, parentMessageId):
        """Initializes the message"""
        self.createdon=datetime.datetime.now()
        self.subject=subject
        self.message=message
        self.status=status
        self.createdby=createdby
        self.address=address
        self.parentMessageId=parentMessageId

    def create_message(self):
        query = "INSERT INTO messages(createdon, subject, message, status, createdby, address)\
            VALUES('{}', '{}', '{}', '{}', '{}', '{}')RETURNING *;".format(
                self.createdon, 
                self.subject,
                self.message,
                self.status, 
                self.createdby,
                self.address)
        cur.execute(query)
        return cur.fetchone()
        

    @staticmethod
    def find_message_by_id(id):
        query = "SELECT * FROM messages WHERE message_id = '{}'".format(id)
        cur.execute(query)
        return cur.fetchone()

    @staticmethod
    def delete_message(id):
        query = "DELETE FROM messages WHERE message_id = {}".format(id)
        cur.execute(query)

    @staticmethod
    def update_status(table_name, status, message_id):
        query = "UPDATE {} SET status = '{}' WHERE message_id = '{}';".format(table_name, status, message_id)
        cur.execute(query) 

    @staticmethod
    def get_all_messages():
        query = "SELECT * FROM messages"
        cur.execute(query)
        return cur.fetchall()
