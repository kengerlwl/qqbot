import nonebot
from os import path
import Config
from nonebot import  session

if __name__ == '__main__':
    nonebot.init(Config)

    # 加载cmd命令插件
    nonebot.load_plugins(
        path.join(path.dirname(__file__), 'plugins','weather'),
        'plugins.weather'
    )

    # bot = nonebot.get_bot()
    nonebot.run(host='127.0.0.1', port=8082)
