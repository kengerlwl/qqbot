# qqbot

## How to start

1. generate project using `nb create` .
2. create your plugin using `nb plugin create` .
3. writing your plugins under `src/plugins` folder.
4. run your bot using `nb run` .


## 运行项目
```
python bot.py
```


## 新增一些插件
可浏览的插件商店
[bot plugin](https://v2.nonebot.dev/store)


## gocqhttp配置

ws接口和一代不一样了
```
# 连接服务列表
servers:
  # 添加方式，同一连接方式可添加多个，具体配置说明请查看文档
  #- http: # http 通信
  #- ws:   # 正向 Websocket
  #- ws-reverse: # 反向 Websocket
  #- pprof: #性能分析服务器
  # 反向WS设置

  - http: # HTTP 通信设置
      address: 0.0.0.0:5700 # HTTP监听地址
      timeout: 5      # 反向 HTTP 超时时间, 单位秒，<5 时将被忽略
      long-polling:   # 长轮询拓展
        enabled: false       # 是否开启
        max-queue-size: 2000 # 消息队列大小，0 表示不限制队列大小，谨慎使用
        
  - ws-reverse:
      universal: ws://127.0.0.1:8082/onebot/v11/ws
      # 反向WS API 地址

      # 重连间隔 单位毫秒
      reconnect-interval: 3000
      middlewares:
        <<: *default # 引用默认中间件
```

## 一个简单插件的编写

```
from nonebot import on_command
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
from nonebot.permission import SUPERUSER

__plugin_name__ = 'print'
__plugin_usage__ = '用法： print管理员给出的话语，测试机器人是否工作。'

# on_command()为针对命令型事件的响应，即以配置的命令前缀为开头的语句
# permission设置为该命令只对bot管理员响应，rule设置为只有私聊或者直接艾特bot时才会生效，priority设置执行优先级为10
# 同一优先级的事件响应器会同时执行，优先级数字越小越先响应！优先级请从 1 开始排序！
pprint = on_command("print", permission=SUPERUSER, rule=to_me(), priority=10, aliases={"打印"})
# pprint = on_command("print",  aliases={"打印"})


# 具体响应逻辑部分
@pprint.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
    # 获取去除了命令前缀后的信息，并且用strip()去除前后的空格与换行符
    msg = str(event.get_message()).strip()
    # print(msg)
    # finish会向信息来源发回作为参数的字符串，并且在执行后结束响应
    # 如果希望发送后继续执行代码，应该将finish改为send
    await pprint.send(msg)

    await pprint.finish("copy")


```


# ref

[一篇实践博客](https://blog.chrisyy.top/qq-chatGPT.html)
