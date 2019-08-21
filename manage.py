#-*- coding: utf-8 -*-
# Author: ARCHer
# Blog: https://www.liudalao.com/
from app import app

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=80,
        debug=True
    )
