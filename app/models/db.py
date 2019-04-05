import os
from app import app
from app import config
import psycopg2
from psycopg2.extras import RealDictCursor
from pprint import pprint

class DatabaseConnection():   
    def __init__(self): 
        self.commands=(
            """CREATE TABLE IF NOT EXISTS users (
            user_id serial primary key, 
            firstname varchar(50) not null,
            lastname varchar(50) not null,
            email varchar(100) not null unique,
            password varchar(200) not null,
            registered_on TIMESTAMP )
            """,
            """CREATE TABLE IF NOT EXISTS messages (
            message_id serial primary key, 
            subject varchar(100) not null,
            message text not null,
            status varchar(100) not null,
            createdby VARCHAR REFERENCES users(email),
            parentMessageId integer default 0,
            createdon TIMESTAMP,
            address VARCHAR not null)
            """,
            """CREATE TABLE IF NOT EXISTS groups(
                group_id serial primary key,
                group_name VARCHAR(50) not null unique,
                role VARCHAR(100) not null,
                createdon TIMESTAMP,
                createdby VARCHAR REFERENCES users(email)
            )""",
            """
                CREATE TABLE IF NOT EXISTS groupmembers(
                    member_id serial primary key,
                    group_id VARCHAR REFERENCES groups(group_name),
                    member VARCHAR REFERENCES users(email),
                    createdon TIMESTAMP WITHOUT TIME ZONE DEFAULT CURRENT_TIMESTAMP
                )
            """,
            """CREATE TABLE IF NOT EXISTS groupmails(
                id serial primary key,
                group_name VARCHAR REFERENCES groups(group_name),
                createdon TIMESTAMP WITHOUT TIME ZONE DEFAULT CURRENT_TIMESTAMP,
                subject varchar(100) not null,
                message text not null,
                status varchar(10) not null,
                createdby VARCHAR REFERENCES users(email)
                )"""
        )
        try:
            if os.getenv("FLASK_ENV") == "production":
                self.connection = psycopg2.connect(os.getenv("DATABASE_URL"), 
                cursor_factory=RealDictCursor)

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
            for command in self.commands:
                self.cursor.execute(command)

        except(Exception, psycopg2.DatabaseError) as error:
                print ("Error while conneccting to PostgreSQL", error)

    def drop_tables(self):
        query = "DROP TABLE IF EXISTS {} CASCADE"
        tabl_names = ["users", "messages", "groupmails", "groups", "groupmembers"]
        for name in tabl_names:
            self.cursor.execute(query.format(name))

    def create_tables(self):
        for command in self.commands:
            self.cursor.execute(command)