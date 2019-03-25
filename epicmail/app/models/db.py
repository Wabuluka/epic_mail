import os
from epicmail.app import app
from epicmail.app import config
import psycopg2

class DatabaseConnection():   
    def __init__(self):     
        try:
            self.connection = psycopg2.connect(user="postgres",
                                                password="root123",
                                                host="127.0.0.1",
                                                port="5432",
                                                database="challengethree")
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
