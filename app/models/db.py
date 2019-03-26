import os
from app import app
from app import config
import psycopg2
from psycopg2.extras import RealDictCursor
from pprint import pprint

class DatabaseConnection():   
    def __init__(self):     
        try:
            self.connection = psycopg2.connect(user="postgres",
                                                password="root123",
                                                host="127.0.0.1",
                                                port="5432",
                                                database="challengethree"
                                                )
            self.connection.autocommit = True
            self.cursor = self.connection.cursor(cursor_factory=RealDictCursor)


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
            createdon TIMESTAMP,
            address varchar(200) not null)"""
        )
        self.cursor.execute(self.messages)

    def drop_tables(self):
        query = "DROP TABLE IF EXISTS {} CASCADE"
        tabl_names = ["users", "messages"]
        for name in tabl_names:
            self.cursor.execute(query.format(name))
