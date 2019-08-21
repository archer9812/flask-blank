#-*- coding: utf-8 -*-
# Author: ARCHer
# Blog: https://www.liudalao.com/
from flask import Flask
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SECRET_KEY"] = "SECRET"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["SQLALCHEMY_COMMIT_ON_TEARDOWN"] = True
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=3)

db = SQLAlchemy(app)


from app.views.admin import admin as admin_blueprint
from app.views.user import user as user_blueprint
from app.views.index import index as index_blueprint

app.register_blueprint(admin_blueprint, url_prefix='/admin')
app.register_blueprint(user_blueprint, url_prefix='/user')
app.register_blueprint(index_blueprint)