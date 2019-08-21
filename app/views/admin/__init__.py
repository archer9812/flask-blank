#-*- coding: utf-8 -*-
# Author: ARCHer
# Blog: https://www.liudalao.com/
from flask import blueprints

admin = blueprints.Blueprint("admin", __name__)

import app.views.admin.views