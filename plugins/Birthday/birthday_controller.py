from nonebot import on_command, CommandSession, on_natural_language, IntentCommand, NLPSession
from plugins.Birthday.birthday_service import *
import re


# on_command 装饰器将函数声明为一个命令处理器
@on_command('birthday', aliases=('生日'))
async def birthday(session: CommandSession):
    msg = "查询任务列表：birthday_search\n" \
          "新增提醒任务：birthday_add\n" \
          "删除提醒任务：birthday_del"
    await session.send(msg)



@on_command('birthday_search',)
async def birthday_search(session: CommandSession):
    # 取得消息的内容，并且去掉首尾的空白符
    req_msg = session.current_arg_text.strip()

    user_id = session.event.user_id
    user = UserService(user_id)
    ans = user.get_all_tasks()
    for i in ans:
        await session.send(str(i))


@on_command('birthday_add')
async def birthday_add(session: CommandSession):
    # 取得消息的内容，并且去掉首尾的空白符
    req_msg = session.current_arg_text.strip()

    # 进行日期匹配
    reg = "^(1[0-2]|[1-9])-(3[01]|[12][0-9]|[1-9])*:.*$"

    # s = '6-29:lwl'
    ans = re.search(reg, req_msg)

    rsp_msg = "success add task"

    if ans != None:

        # 提取数字
        # pattern2 = "\d+"
        # date = re.findall(pattern2, req_msg)

        date =  req_msg.split(':')[0]
        to_user = req_msg.split(':')[1]
        # 添加到数据库
        user_id = session.event.user_id
        user = UserService(user_id)
        user.task_add(date, to_user)
        print(date, to_user)
    else:
        rsp_msg = 'fail, your farmot is wrong'


    await session.send(rsp_msg)


@on_command('birthday_del')
async def birthday_del(session: CommandSession):
    # 取得消息的内容，并且去掉首尾的空白符
    task_id = session.current_arg_text.strip()
    user_id = session.event.user_id
    user = UserService(user_id)

    user.task_delete(task_id)

    await session.send("delete success")
