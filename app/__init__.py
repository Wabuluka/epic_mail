import os

from flask import Flask
from flask_bcrypt import Bcrypt
from flask_jwt_extended import (
    JWTManager, create_access_token,
    get_jwt_identity
)
from flask_cors import CORS
from flasgger import Swagger

app = Flask(__name__)


app_settings = os.getenv(
    'APP_SETTINGS',
    'app.config.DevelopmentConfig'
)

app.config.from_object(app_settings)

bcrypt = Bcrypt(app)
jwt = JWTManager(app)
cors = CORS(app)
swag=Swagger(app)

# calling the blueprints
from app.views.user_views import user_blueprint
from app.views.message_views import messages_blueprint
from app.views.group_views import groups_blueprint

# registering the blueprints
app.register_blueprint(user_blueprint, url_prefix='/api/v2/')
app.register_blueprint(messages_blueprint, url_prefix='/api/v2/')
app.register_blueprint(groups_blueprint, url_prefix='/api/v2/')