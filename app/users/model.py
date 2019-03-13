# users/model.py
from werkzeug.security import generate_password_hash, check_password_hash

users = []

class User:
    """User Model contains the properties stored for a user"""

    def __init__(self, id, email, firstname, lastname, password_hash):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password_hash = generate_password_hash(password_hash)

    def to_dictionary(self):
        return {
            "id":self.id,
            "firstname":self.firstname,
            "lastname":self.lastname,
            "email":self.email,
            "password":self.password_hash
        }
