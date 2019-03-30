import datetime
from app.models.db import DatabaseConnection

database=DatabaseConnection()
cur=database.cursor

class Group:
    
    def __init__(self, **kwargs):
        self.group_name=kwargs['group_name']
        self.role=kwargs['role']
        self.createdby=kwargs['createdby']
        self.createdon=datetime.datetime.now()

    @staticmethod
    def check_groupname_existance(group_name):
        """Check if a group exists"""
        query="SELECT * FROM groups WHERE group_name='{}'".format(group_name)
        cur.execute(query)
        return cur.fetchone()
    
    def create_group(self):
        """Create a group"""
        query="INSERT INTO groups(group_name, role, createdon, createdby)\
            VALUES('{}','{}','{}',{})RETURNING *;".format(
                self.group_name,
                self.role,
                self.createdon,
                self.createdby      
            )
        cur.execute(query)
        return cur.fetchone()
    
    @staticmethod
    def delete_group(id, createdby):
        """Delete a group created"""
        query = "DELETE FROM groups WHERE group_id = {} AND createdby ='{}'".format(id, createdby)
        cur.execute(query)

    @staticmethod
    def add_member(group_id, member):
        """Add a member to a group"""
        query="INSERT INTO groupmembers(group_id, member)\
            VALUES({},{}) RETURNING *;".format(
                group_id, member
            )
        cur.execute(query)
        return cur.fetchone()

    @staticmethod
    def delete_user(group_id, member):
        """Remove a member of a group"""
        query="DELETE FROM groupmembers WHERE group_id= {} AND member = {}".format(group_id, member)
        cur.execute(query)

    @staticmethod
    def create_group_message(group_id,subject,message,status,createdby):
        """Create a message in the group"""
        query="INSERT INTO groupmails(group_id,subject,message,status,createdby)VALUES({},'{}','{}','{}',{})".format(
            group_id,subject,message,status,createdby
        )
        cur.execute(query)
