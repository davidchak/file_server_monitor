# coding: utf8

from flask import Flask
from config import DevConfig
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config.from_object(DevConfig)
db = SQLAlchemy(app)

from app import routes, models