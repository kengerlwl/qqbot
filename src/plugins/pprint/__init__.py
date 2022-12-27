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

