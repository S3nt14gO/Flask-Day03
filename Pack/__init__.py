import os

from flask import Flask, render_template , url_for,redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from flask_migrate import Migrate
from flask_login import LoginManager
# from .models import *
app = Flask(__name__)

app.config['SECRET_KEY'] = '92bb1cc78650ae59ae9b8266bac43d93'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'


convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

metadata = MetaData(naming_convention=convention)
db = SQLAlchemy(app, metadata=metadata)

migrate = Migrate(app,db, render_as_batch=True)

login_manager = LoginManager(app)

from Pack import routes
from Pack.routes import stds
app.register_blueprint(stds)