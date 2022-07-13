import random
import re
import string
import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder

import json
url = "http://127.0.0.1:80/api/birthdays/task_add"


data = { 'username': 'lwl',
     'birthday_time': '4-11',
     'hour': '9',
     'minute': '13',
     'to_user': 'ssd',
     'email': '2892211452',
     'task_type': 'qqbot'
}



m = MultipartEncoder(
        fields=data
    )

headers = {'Content-Type': m.content_type, 'accept': 'application/json'}

rsp = requests.post(url,  data=m, headers=headers)
print(rsp.text)