from flask import Flask
from flask_restful import Api
from src.SpecialMath import SpecialMath


def initialize_api():
    app = Flask('Special Math')
    api = Api(app)
    api.add_resource(SpecialMath, '/specialmath/<string:number>')

    return app
