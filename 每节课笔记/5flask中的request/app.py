# coding:utf-8

from flask import Flask, request

app = Flask(__name__)


# 这种是一个接口 api
@app.route("/index", methods=["GET", "POST"])
def index():
    # request中包含了前端发送过来的所有请求数据
    # form和data是用来提取请求体数据
    # 通过request.form可以直接提取请求体中的表单格式的数据，是一个类字典的对象
    # 通过get方法只能拿到多个同名参数的第一个
    name = request.form.get("name", "zhangsan")  # 设置默认值，如果没有name默认为张三
    age = request.form.get("age")
    name_li = request.form.getlist("name")   # 可以通过getlist提取多个同名的参数
    print(request.data)

    # args是用来提取url中的参数（查询字符串）
    city = request.args.get("city")
    return "index page hello name = %s, age = %s, city = %s, name_li = %s" % (name, age, city, name_li)
    # 如果从前端发送过来的数据不是表单格式，例如在postman中使用row
    # 发送json格式的数据，那么我们可以在data中获取数据，而参数form则获取不到数据

# 惊了，在url中可以传任何参数，不仅限get请求的参数，也可以是别的请求
# 例如在127.0.0.1:5000/index?city=shengzhen  在？后面的部分叫做“查询字符串”，英文文档中为“QueryString”
# 这部分可以是request中参数args来提取


if __name__ == '__main__':
    app.run()
