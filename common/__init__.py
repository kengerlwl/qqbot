from .农历生日计算与提醒判断 import *
from .Tool_Fun import *

from flask import request
from flask import jsonify


rsp_code = {
    "OK": 92000,
    "Bad Request": 94000,
    "Forbidden": 94030,
    "Not Found": 94040,
    "Internal Server Error": 95000,
    "Bad Gateway": 95020
}


def common_rsp(data, status='OK'):
    if status in rsp_code.keys():
        code = rsp_code[status]
    else:
        code = 95001
    rsp_format = request.args.get('format')
    if rsp_format == 'raw':  # 如果指定了数据格式
        return data
    else:
        return jsonify({
            'code': code,
            'status': status,
            'time': unix_time(),
            'method': func_name(2),  # 出错的方法名
            'timestamp': str_time(),
            'data': data
        })
