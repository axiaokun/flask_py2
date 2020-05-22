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
    # 2. 通过current_app获取参数
    return "hello flask"


if __name__ == '__main__':
    # 启动flask程序

    # run参数设置，可配置访问地址和端口
    # 注意一个知识0.0.0.0，0.0.0.0是不能被ping通的。在服务器中，0.0.0.0并不是一个真实的的IP地址，它表示本机中所有的IPV4地址。监听0.0.0.0的端口，就是监听本机中所有IP的端口
    app.run(host='0.0.0.0', port='5000')
