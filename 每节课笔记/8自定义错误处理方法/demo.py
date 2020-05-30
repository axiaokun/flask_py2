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


# 定义错误处理的方法
@app.errorhandler(404)
def handle_404_error(err):
    """自定义的处理错误方法"""
    # 这个函数的返回值会是前端用户看到的最终结果
    return u"出现404错误，错误信息： %s" % err


if __name__ == '__main__':
    app.run(debug=True)
