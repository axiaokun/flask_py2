# coding: utf-8


# 请求钩子  钩子相当于Django中的中间件
from flask import Flask, request

app = Flask(__name__)


@app.route("/index")
def index():
    print("index 被执行")
    raise TabError
    return "index page"


@app.route("/hello")
def hello():
    print("hello 被执行")
    return "hello page"


@app.before_first_request
def handle_before_first_request():
    """在第一次请求处理之前被执行"""
    print("handle_before_first_request 被执行")


@app.before_request
def handle_before_request():
    """在每次请求之前都会被执行"""
    print("handle_before_request")


@app.after_request
def handle_after_request(response):
    """在每次请求（被视图函数处理）之后都被执行， 前提是视图函数没有出现异常"""
    print("handle_after_request   被执行")
    return response


@app.teardown_request
def handle_teardown_request(response):
    """"在每次请求（被视图函数处理）之后都被执行, 无论视图函数是否出现异常"""
    print("handle_teardown_request  被执行")
    print(request.args)
    return response


if __name__ == '__main__':
    app.run(debug=True)

