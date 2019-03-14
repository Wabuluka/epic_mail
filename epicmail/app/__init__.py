import os

from flask import Flask

app = Flask(__name__)


app_settings = os.getenv(
    'APP_SETTINGS',
    'epicmail.app.config.DevelopmentConfig'
)

app.config.from_object(app_settings)