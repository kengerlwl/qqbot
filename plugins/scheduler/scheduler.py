from datetime import datetime
from plugins.Birthday import *
import nonebot
import pytz
from aiocqhttp.exceptions import Error as CQHttpError
from common import *


# 定时执行任务
@nonebot.scheduler.scheduled_job('cron', hour='*', minute="55", second="0" )
async def birthday_check():
    bot = nonebot.get_bot()
    now = datetime.now(pytz.timezone('Asia/Shanghai'))
    try:

        # 获取所有的好友
        all_friends = await bot.get_friend_list()
        # {'nickname': '风格', 'remark': '风格', 'user_id': 1499427353},]

        # 对数据库中所有任务进行遍历
        users = get_all_user()
        # print(users)
        for user_id, _,__ in users:
            user = UserService(user_id)
            tasks = user.get_all_tasks()
            # 构建需要提醒的任务列表
            lists = []
            # 遍历所有任务
            for task_id, date, to_user in tasks:
                lists.append([date, to_user, user_id])
            # print(lists)
            remainder(lists)
            # await bot.send_private_msg(user_id=2892211452, message="test")
    except CQHttpError:
        pass


"""
# 定时执行任务
@nonebot.scheduler.scheduled_job('cron', hour='1', minute="0", second="*" )
async def _():
    bot = nonebot.get_bot()
    now = datetime.now(pytz.timezone('Asia/Shanghai'))
    try:

        # 获取所有的好友
        # users = await bot.get_friend_list()
        # {'nickname': '风格', 'remark': '风格', 'user_id': 1499427353},]
        # 获取所有群
        # groups = await bot.get_group_list()
        #[{'group_create_time': 0, 'group_id': 519467053, 'group_level': 0, 'group_name': '行者、kengerbot', x_member_count': 200, 'member_count': 2}]

        # groups = await bot.get_
        # print(groups)
        await bot.send_private_msg(user_id=2892211452, message="test")
    except CQHttpError:
        pass
"""
