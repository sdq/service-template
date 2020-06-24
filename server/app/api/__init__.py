from flask import Blueprint
from flask_restful import Api
from .service import Service

api_blueprint = Blueprint("api", __name__, url_prefix = '/service')
api = Api(api_blueprint)

api.add_resource(Service, '/yourapiname') # replace with your api name