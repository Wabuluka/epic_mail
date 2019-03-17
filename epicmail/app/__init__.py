import os

from flask import Flask
from flask_bcrypt import Bcrypt

app = Flask(__name__)


app_settings = os.getenv(
    'APP_SETTINGS',
    'epicmail.app.config.DevelopmentConfig'
)

app.config.from_object(app_settings)

bcrypt = Bcrypt(app)

# calling the blueprints
from epicmail.app.users.views import user_blueprint
from epicmail.app.messages.views import messages_blueprint

# registering the blueprints
app.register_blueprint(user_blueprint, url_prefix='/epicmail/api/v2/')
app.register_blueprint(messages_blueprint, url_prefix='/epicmail/api/v2/')