from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import DevConfig

app = Flask(__name__)
app.config.from_object(DevConfig)

db = SQLAlchemy(app)

from app import models

db.create_all()

def get_db_session() -> db.Session:
    return db.session


from .api import blueprint_api 

app.register_blueprint(blueprint_api, subdomain='api')


from .routers import *

app.register_blueprint(example_blueprint)
