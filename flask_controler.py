# coding=utf-8
import os
import logging
from logging.handlers import TimedRotatingFileHandler

from flask import Flask
from flask import request
from flask_cors import CORS
import os
from flask import Blueprint
import json
from Config import *
from common import *
import common as Kit

app = Flask(__name__)



def init_app():
    # 服务日志
    # 创建日志目录
    if not os.path.exists('./log/'):
        os.makedirs('./log/')

    # 设置日志格式
    formatter = logging.Formatter(
        "[%(asctime)s][%(filename)s:%(lineno)d][%(levelname)s][%(thread)d] - %(message)s")
    handler = TimedRotatingFileHandler(
        "./log/run.log", when="D", interval=1, backupCount=15,
        encoding="UTF-8", delay=False, utc=True)
    app.logger.addHandler(handler)
    handler.setFormatter(formatter)



    app.Config = get_config()



    # 设置跨域访问
    CORS(app, supports_credentials=True)


# 多个url可以指向同一个函数
@app.route('/')
@app.route('/api')
def hello_world():
    return '<h1>hello world main page<h1>'



# Kit数据测试函数
@app.route('/testData', methods=['GET'])
def data_test():
    rsp_data = 'hello data'
    return Kit.common_rsp(rsp_data)


@app.route('/api/generate_204')
@app.route('/generate_204')
def network_test():
    return str("success"), 204


@app.route('/debug/sentry')
def sentry_debug():
    app.logger.info("[DEBUG]Test sentry: {}".format(1 / 0))
    return Kit.common_rsp("DEBUG")


@app.errorhandler(400)
def http_forbidden(msg):
    app.logger.warning("{}: <HTTP 400> {}".format(request.url, msg))
    return Kit.common_rsp("Bad Request", status='Bad Request')


@app.errorhandler(403)
def http_forbidden(msg):
    app.logger.error("{}: <HTTP 403> {}".format(request.url, msg))
    return Kit.common_rsp(str(msg)[15:], status='Forbidden')


@app.errorhandler(404)
def http_not_found(msg):
    app.logger.error("{}: <HTTP 404> {}".format(request.url, msg))
    return Kit.common_rsp(str(msg)[15:], status='Not Found')


@app.errorhandler(500)
def service_error(msg):
    app.logger.error("{}: <HTTP 400> {}".format(request.url, msg))
    return Kit.common_rsp(str(msg)[15:], status='Internal Server Error')



from plugins.Birthday import *

# 接来下开始正经三个函数

# 多个url可以指向同一个函数
@app.route("/<user_id>", methods=['GET'])
def birthday_search(user_id=None):
    if user_id == None:
        return '<h1>get<h1>'
    elif user_id == 'all':
        return 'all'
    else:

        user = UserService(user_id)
        tasks = user.get_all_tasks()

        rsp = {
            'user':user_id,
            'tasks':tasks
        }
        return Kit.common_rsp(rsp)



@app.route("/task_add", methods=['POST'])
def birthday_add():

    # print(request.form)
    data = request.form
    data = dict(data)
    user = UserService(data['username'])
    task_id = user.task_add(data['birthday_time'],data['to_user'])
    app.logger.info(data['username'] + ' 新增了任务 ' + task_id)
    rsp = {
        'task_id':task_id
    }

    return Kit.common_rsp(rsp)



@app.route("/task_delete", methods=['POST'])
def birthday_delete():
    data = request.form

    task_id = data['task_id']
    user_id = data['username']
    user = UserService(user_id)
    user.task_delete(task_id)


    msg = 'success'

    rsp = {
        'answer': msg
    }

    return Kit.common_rsp(rsp)



# 用于gunicorn启动时的初始化
if __name__ != '__main__':
    init_app()  # 进行初始化配置

    app.logger.setLevel(logging.DEBUG)




if __name__ == '__main__':
    init_app()  # 进行初始化配置

    app.logger.setLevel(logging.DEBUG)
    app.run(host='0.0.0.0', port=82, debug=True)
    exit()
