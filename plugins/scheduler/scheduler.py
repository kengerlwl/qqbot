from datetime import datetime

import nonebot
import pytz
from aiocqhttp.exceptions import Error as CQHttpError


@nonebot.scheduler.scheduled_job('cron', hour='*', minute="*" )
async def _():
    bot = nonebot.get_bot()
    now = datetime.now(pytz.timezone('Asia/Shanghai'))
    try:
        await bot.send_private_msg(user_id=2892211452, message="test")
    except CQHttpError:
        pass