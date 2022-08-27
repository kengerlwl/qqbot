# borax==3.3.1
import copy

from borax.calendars.lunardate import LunarDate
import requests
from Config import *

conf = get_config()


def send_msg_to_qq(msg, qq_num):
    conf = get_config()
    host = conf['qq_server']['host']
    port = conf['qq_server']['port']
    url = "http://{}:{}/send_private_msg?user_id={}&message={}".format(host, port, qq_num, msg)
    requests.get(url=url)




def remainder(list):
    # list = [
    #     ['12-25', 'test1']  #第一个是农历生日，第二个是名字
    # ]

    # 获取今天的农历日期
    today = LunarDate.today()

    year = today.year
    month = today.month
    day = today.day

    for i, name, reciver in list:

        i = i.split('-')
        tmpMonth = int(i[0])
        tmpDay = int(i[1])
        tmpNow = LunarDate(year, tmpMonth, tmpDay)  # 今年的生日日期
        if tmpNow < today:
            tmpNow = LunarDate(year+1, tmpMonth, tmpDay)  # 明年的生日日期
        # print(tmpNow)
        dis = today - tmpNow
        dis = dis.days



        message = None
        if  dis == 0:
            message = '今天'
        elif dis == -1:
            message = '明天'
        elif dis == -2:
            message = '后天'
        elif dis == -3:
            message = '大后天'

        # print(message, dis)

        # 若在范围内
        if message:
            # 转化为公历
            solarDay = tmpNow.to_solar_date()
            try:
                message= message + '是' + name + '的生日' +'  具体日期是: '+ str(solarDay)
                send_msg_to_qq(message,reciver)
            except:
                pass


        else:
            print(name+ '的生日 今天不需要通知')



if __name__ == '__main__':
    list = [
        ['6-29', 'test1', '2892211452']  #第一个是农历生日，第二个是名字，第三个是号码
    ]
    remainder(list)
