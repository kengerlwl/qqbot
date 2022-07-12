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

    # 加载我的生日插件
    nonebot.load_plugins(
        path.join(path.dirname(__file__), 'plugins','Birthday'),
        'plugins.Birthday'
    )


    # 这里的ip要用0.0.0.0,不然不能和外部进行连接
    nonebot.run(host='0.0.0.0', port=8082)
