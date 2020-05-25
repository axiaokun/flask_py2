# coding:utf-8

from flask import Flask, redirect, url_for

# 创建flask的应用对象
# __name__ 表示当前的模块名字
#                模块名。flask以这个模块所在的目录为总目录，默认这个目录中的static为静态目录，templates为模板目录
app = Flask(__name__,
            static_url_path='/python')  # 设置前缀


@app.route("/")  # 指定url
def index():
    """定义视图函数"""
    return "hello flask"


# 本节课第二点内容
# add view function
@app.route("/post_only", methods=["POST", "GET"])  # add resquest method
def post_only():
    return "post only page"


# 本节课第三点内容
# 两个视图函数使用同一个路径
@app.route("/hello")
def hello():
    return "hello1"


@app.route("/hello")
def hello2():
    return "hello2"
# 测试结果可以看到，在下面路由信息中都包含这两个路径，但是只能访问到排在前面的hello函数
# 如何能够访问到第二个： 可以使用methods方法修改请求方式，使得两个视图函数的请求方法不一样


# 本节课第四点内容
# 不同的路径使用同个视图函数
@app.route("/hi")
@app.route("/hi1")
def hi():
    return "HI!"


# 本节课第五点重定向跳转页面
@app.route("/login")
def login():
    # url = "/" 使用变量写入url，写死的方式，不建议，要是原来的视图函数一改就完蛋了
    # 使用url_for的函数，通过视图函数的名字找到视图对应的url路径
    url = url_for("index")
    return redirect(url)  # 重定位函数


if __name__ == '__main__':
    # 本节课第一点内容
    # 通过url_app可以查看整个flask中的路由信息
    print(app.url_map)
    # 启动flask程序
    app.run()
