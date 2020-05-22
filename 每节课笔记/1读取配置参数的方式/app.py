# coding:utf-8

from flask import Flask, current_app

# 创建flask的应用对象
# __name__ 表示当前的模块名字
#                模块名。flask以这个模块所在的目录为总目录，默认这个目录中的static为静态目录，templates为模板目录
app = Flask(__name__,
            static_url_path='/python')  # 设置前缀

# 使用对象配置参数
class Config(object):
    DEBUG = True
    ITCAST = 'python'

app.config.from_object(Config)

@app.route("/")  # 指定url
def index():
    """定义视图函数"""
    # 读取配置参数
    # 1. 直接从全局对象app的config字典中取值
    print(app.config.get("ITCAST"))
    # 2. 通过current_app获取参数
    print(current_app.config.get('ITCAST'))
    return "hello flask"


if __name__ == '__main__':
    # 启动flask程序
    app.run()
