from plugins.Birthday.birthday_dao import *
import uuid
import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder
import json
from Config import *



class UserService():
    def __init__(self):
        self.user_id =None
    def __init__(self, user_id):
        self.user_id =user_id

    def task_add(self, date, to_user):
        """
        :param date:  时间
        :param to_user: 当天生日的人
        :return:  返回生成任务的id
        """

        task_id = uuid.uuid1()
        task_creaat(task_id, date, to_user)
        user_task_creat(self.user_id, task_id)
        return str(task_id)



    def task_delete(self, task_id):
        task_delete(task_id)
        user_task_delete(task_id)


    def all_task_delete(self):
        tasks = user_task_search(self.user_id)
        for u,task_id in tasks:
            self.task_delete(task_id)

    def get_all_tasks(self):
        tasks = user_task_search(self.user_id)
        ans = []
        for u,task_id in tasks:
            task = task_search(task_id)
            ans.append(task)
        return ans



if __name__ == '__main__':
    lwl = UserService(2892211452)
    lwl.task_add('date', 'kong')
    lwl.task_add('date2', 'kong2')

    ans = lwl.get_all_tasks()
    print(ans)
