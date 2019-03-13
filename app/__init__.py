from flask import Flask

app = Flask(__name__)

from app.users.view import user_bp

app.register_blueprint(user_bp)