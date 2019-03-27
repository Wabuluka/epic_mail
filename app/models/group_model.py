import datetime
from app.models.db import DatabaseConnection

database=DatabaseConnection()
cur=database.cursor
database.create_groups_table()
database.create_group_members_table()

class Group:
    def __init__(self, **kwargs):
        self.group_name=kwargs['group_name']
        self.role=kwargs['role']
        self.createdby=kwargs['createdby']
        self.createdon=datetime.datetime.now()

    @staticmethod
    def check_groupname_existance(group_name):
        query="SELECT * FROM groups WHERE group_name='{}'".format(group_name)
        cur.execute(query)
        return cur.fetchone()
    
    def create_group(self):
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
        query = "DELETE FROM groups WHERE group_id = {} AND createdby ='{}'".format(id, createdby)
        cur.execute(query)

    @staticmethod
    def add_member(group_id, member):
        query="INSERT INTO groupmembers(group_id, member)\
            VALUES({},{}) RETURNING *;".format(
                group_id, member
            )
        cur.execute(query)
        return cur.fetchone()

    @staticmethod
    def delete_user(member):
        query="DELETE FROM groupmembers WHERE member = {}".format(member)
        cur.execute(query)
