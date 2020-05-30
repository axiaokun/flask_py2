# coding: utf-8

from flask import Flask
from flask_script import Manager  # 启动命令的管理类

app = Flask(__name__)

manager = Manager(app)  # 创建管理对象


@app.route("/index")
def index():
    return "index page"


if __name__ == '__main__':
    # app.run(debug=True)
    manager.run()  # 通过这个管理对象来启动
