#-*- coding: utf-8 -*-
# Author: ARCHer
# Blog: https://www.liudalao.com/
from flask import blueprints

user = blueprints.Blueprint("user", __name__)

import app.views.user.views