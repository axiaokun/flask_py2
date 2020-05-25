# coding:utf-8

from flask import Flask, request, abort, Response

app = Flask(__name__)


@app.route("/login", methods=["GET"])
def login():
    # 获取登录信息
    # name = request.form.get()
    # pwd = request.form.get()

    # 这里先用空字符代替
    name = ""
    pwd = ""

    if name != "zhangsan" or pwd != "admin":
        # 使用abort函数可以立即终止函数的执行
        # 并可以返回给前端特定的信息
        # 1. 传递状态码， 必须是标准的HTTP状态码
        abort(404)
        # # 2. 传递响应体信息
        # resp = Response("login failure")
        # abort(resp)
    return "login success"


if __name__ == '__main__':
    app.run(debug=True)
