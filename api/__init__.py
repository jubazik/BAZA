from config import Config
from flask import Flask, request, jsonify, json, g
from flask_restful import Api, Resource, reqparse
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import datetime

date = datetime.datetime.now()
app = Flask(__name__)
app.config.from_object(Config)
api = Api(app)
db = SQLAlchemy(app)




migrate = Migrate(app, db)