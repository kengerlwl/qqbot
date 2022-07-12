import sqlite3
import os
Fir = os.getcwd()
# print(Fir)

def get_con():
    db_path = Fir + '/plugins/Birthday/db/birthday.db'
    # print(db_path)
    # 不存在就创建文件
    if not os.path.exists(db_path):
        open(db_path)
    conn = sqlite3.connect(db_path)
    return conn

def init():
    # 创建表
    conn = get_con()

    c = conn.cursor()
    c.execute('''CREATE TABLE user
           (user_id INT PRIMARY KEY     NOT NULL,
           nickname           CHAR(50),   
           remark            CHAR(50)
           );''')
    print ("user数据表创建成功")

    c.execute('''CREATE TABLE task
           (task_id CHAR(50) PRIMARY KEY     NOT NULL,
           date           CHAR(50),
           to_user        CHAR(50)
           );''')
    print ("task数据表创建成功")


    c.execute('''CREATE TABLE user_task
           (user_id INT     NOT NULL,
           task_id           CHAR(50)
           );''')
    print ("user-task数据表创建成功")

    conn.commit()
    conn.close()

def user_creat(user_id, nickname, remark):
    conn = get_con()
    c = conn.cursor()

    #为了解决字符串插入问题，建议全部改成这种格式化
    ex_sql = "INSERT INTO user (user_id,nickname,remark) VALUES ({}, '{}','{}')"
    ex_sql =ex_sql.format(user_id, nickname, remark)

#    print(ex_sql)
    c.execute(ex_sql)
    conn.commit()
    conn.close()

def task_creaat(task_id, date, to_user):
    conn = get_con()
    c = conn.cursor()

    # 为了解决字符串插入问题，建议全部改成这种格式化
    ex_sql = "INSERT INTO task (task_id,date,to_user) VALUES ('{}', '{}', '{}')"

    ex_sql = ex_sql.format(task_id, date,to_user)

    print(ex_sql)
    c.execute(ex_sql)
    conn.commit()
    conn.close()


def task_delete(task_id):
    conn = get_con()
    c = conn.cursor()

    # 为了解决字符串插入问题，建议全部改成这种格式化
    ex_sql = "DELETE FROM task where task_id = '{}'"
    ex_sql = ex_sql.format(task_id)

    c.execute(ex_sql)
    conn.commit()
    conn.close()


def task_search(task_id):
    conn = get_con()
    c = conn.cursor()

    # 为了解决字符串插入问题，建议全部改成这种格式化
    ex_sql = "SELECT task_id, date , to_user FROM task where task_id = '{}'"
    ex_sql = ex_sql.format(task_id)

    cursor = c.execute(ex_sql)
    ans = []
    for i in cursor:
        # print(i)
        ans.append(i)

    conn.commit()
    conn.close()

    return ans[0]


def user_task_creat(user_id, task_id):
    conn = get_con()
    c = conn.cursor()

    # 为了解决字符串插入问题，建议全部改成这种格式化
    ex_sql = "INSERT INTO user_task (user_id,task_id) VALUES ({}, '{}')"
    ex_sql = ex_sql.format(user_id, task_id)

    c.execute(ex_sql)
    conn.commit()
    conn.close()

def user_task_delete(task_id):
    conn = get_con()
    c = conn.cursor()

    # 为了解决字符串插入问题，建议全部改成这种格式化
    ex_sql = "DELETE FROM user_task where task_id = '{}'"
    ex_sql = ex_sql.format(task_id)

    c.execute(ex_sql)
    conn.commit()
    conn.close()


def user_task_search(user_id):
    conn = get_con()
    c = conn.cursor()

    # 为了解决字符串插入问题，建议全部改成这种格式化
    ex_sql = "SELECT user_id,task_id FROM user_task where user_id = '{}'"
    ex_sql = ex_sql.format(user_id)

    cursor = c.execute(ex_sql)
    tasks = []
    for i in cursor:
        # print(i)
        tasks.append(i)

    conn.commit()
    conn.close()

    return tasks


if __name__ == '__main__':
    init()
    user_creat(2892211452, 'xingzhe', 'lwl')
    task_creaat(1, 'date', 'kong')
    user_task_creat(2892211452,1)
    cursor = user_task_search(2892211452)

    task_delete(1)
    user_task_delete(1)