from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api   # use more flask-utils

from config import DevConfig

app = Flask(__name__)
app.config.from_object(DevConfig)

db = SQLAlchemy(app)

from app import models

db.create_all()


def get_db_session() -> db.Session:
    return db.session


app_api = Api(app)


from app.api.resources import entity

# app_api.add_resource(entity.EntityResource, '/api/entity/<TYPE:PARAMETER>')


from app.api.relations import blueprint_relations

app.register_blueprint(blueprint_relations)
