import json
import logging
from nonebot.default_config import *
import os


SUPERUSERS = {2892211452}# 超级权限用户
# http通信
API_ROOT = 'http://0.0.0.0:5700'  # 这里 IP 和端口应与 go-cqhttp 配置中的 `host` 和 `port` 对应



def get_config(run_env=None):
    # 读取配置文件
    if run_env is None:
        run_env = 'para'
    if 'SERVICE_ENV' in os.environ:
        run_env = os.environ['SERVICE_ENV']
    config_path = '{}/{}.json'.format(os.path.split(os.path.abspath(__file__))[0], run_env)
    # print(config_path)
    # config_path = 'Config/para.json'
    if os.path.isfile(config_path):
        config_data = open(config_path, "r", encoding="utf-8").read()
        app_config = json.loads(config_data)  # 师兄的

        app_config["RUN_ENV"] = run_env
        return app_config
    else:
        logging.error("Config not exist")
        exit()
