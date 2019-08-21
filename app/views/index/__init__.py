#-*- coding: utf-8 -*-
# Author: ARCHer
# Blog: https://www.liudalao.com/
from flask import blueprints

index = blueprints.Blueprint("index", __name__)

import app.views.index.views