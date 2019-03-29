import os
from app import app
from app import config
import psycopg2
from psycopg2.extras import RealDictCursor
from pprint import pprint

class DatabaseConnection():   
    def __init__(self):     
        try:
            if os.getenv("production") == "production":
                self.connection = psycopg2.connect(dbname='dd5fjt4vlqe4u7',
                                                   user='wsldafxguglltc',
                                                   password='fad7e9c808db7d1f53ce9533b54913b4f61f0ecaf371f8d34e75e10c8244f60e',
                                                   host='ec2-54-83-61-142.compute-1.amazonaws.com',
                                                   port='5432', cursor_factory=RealDictCursor)

            elif os.getenv("FLASK_ENV") == "TESTING":
                print('Connecting to test db')
                self.connection = psycopg2.connect(dbname='challengethree_test',
                                                   user='postgres',
                                                   password='',
                                                   host='localhost',
                                                   port='5432', cursor_factory=RealDictCursor)
            else:
                print('Connecting development db')
                self.connection = psycopg2.connect(dbname='challengethree',
                                                   user='postgres',
                                                   password='root123',
                                                   host='localhost',
                                                   port='5432', cursor_factory=RealDictCursor)
            self.connection.autocommit = True
            self.cursor = self.connection.cursor()


        except(Exception, psycopg2.DatabaseError) as error:
                print ("Error while conneccting to PostgreSQL", error)
            
    def create_user_table(self):
        self.users = (
            """CREATE TABLE IF NOT EXISTS users (
            user_id serial primary key, 
            firstname varchar(50) not null,
            lastname varchar(50) not null,
            email varchar(100) not null unique,
            password varchar(200) not null,
            registered_on TIMESTAMP )""")
        self.cursor.execute(self.users)

    def create_messages_table(self):
        self.messages = (
            """CREATE TABLE IF NOT EXISTS messages (
            message_id serial primary key, 
            subject varchar(100) not null,
            message text not null,
            status varchar(100) not null,
            createdby INT REFERENCES users(user_id),
            parentMessageId integer default 0,
            createdon TIMESTAMP,
            address INT not null)"""
        )
        self.cursor.execute(self.messages)

    def create_groups_table(self):
        self.groups=(
            """CREATE TABLE IF NOT EXISTS groups(
                group_id serial primary key,
                group_name VARCHAR(50) not null unique,
                role VARCHAR(100) not null,
                createdon TIMESTAMP,
                createdby INT REFERENCES users(user_id)
            )"""
        )
        self.cursor.execute(self.groups)

    def create_group_members_table(self):
        self.groupmembers=(
            """
                CREATE TABLE IF NOT EXISTS groupmembers(
                    member_id serial primary key,
                    group_id INT REFERENCES groups(group_id),
                    member INT REFERENCES users(user_id),
                    createdon TIMESTAMP WITHOUT TIME ZONE DEFAULT CURRENT_TIMESTAMP
                )
            """
        )
        self.cursor.execute(self.groupmembers)

    def create_group_mail(self):
        self.groupmails=(
            """CREATE TABLE IF NOT EXISTS groupmails(
                id serial primary key,
                group_id INT REFERENCES groups(group_id),
                createdon TIMESTAMP WITHOUT TIME ZONE DEFAULT CURRENT_TIMESTAMP,
                subject varchar(100) not null,
                message text not null,
                status varchar(10) not null,
                createdby INT REFERENCES users(user_id)
                )"""
        )
        self.cursor.execute(self.groupmails)

    def drop_tables(self):
        query = "DROP TABLE IF EXISTS {} CASCADE"
        tabl_names = ["users", "messages", "groupmails", "groups", "groupmembers"]
        for name in tabl_names:
            self.cursor.execute(query.format(name))
