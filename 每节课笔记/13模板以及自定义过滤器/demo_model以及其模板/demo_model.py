# coding: utf-8

from flask import Flask, render_template


app = Flask(__name__)


@app.route("/index")
def index():
    data = {
        "name": "python",
        "age": 18,
        "my_dict": {"city": "sz"},
        "my_list": [1, 2, 3, 4],
        "my_int": 0
    }
    # # flask 中普通的传参给模板渲染网页
    # return render_template("index.html", name="python", age=18)
    # 传字典
    return render_template("index.html", **data)


if __name__ == '__main__':
    app.run(debug=True)
