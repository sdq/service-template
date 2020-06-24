from flask import Flask
from flask_cors import CORS
from config import Config
from .api import api_blueprint

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    CORS(app)
    app.config.from_object(Config)
    app.register_blueprint(api_blueprint, url_prefix = '/service')
    return app