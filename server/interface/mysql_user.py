import os
import sys

from pymysql import NULL
sys.path.append(os.path.abspath(os.path.dirname(__file__)+'/'+'..'))
from database.pymysql_comm import UsingMysql


#-----------------------------------------
# 查询用户 账号 密码 用户名 
# 根据账号得到用户名密码
# 没找到id用户返回null，找到返回用户信息
def fetch_user_by_filter(cursor, id):
    sql = f'select * from user where id = {id}' 
    cursor.execute(sql)
    data_dict = cursor.fetchall()
    if len(data_dict) == 0:
        return NULL
    # print('-- 查询 账号 密码 用户名 : %s' %data_dict[0])
    return data_dict[0]
# 查找
def fetch_user(id):

    with UsingMysql(log_time=False) as um:
        data_dict = fetch_user_by_filter(um.cursor, id)
    return data_dict
#----------------------------
# 添加用户（账号 密码 用户名）

def create_one(id, name, password):

    with UsingMysql(log_time=False) as um:
        sql = "insert into user(id, name, password, state, friends, message) values(%s, %s, %s, %s, %s, %s)"
        params = (str(id), str(name), str(password), '0', '','{}')
        um.cursor.execute(sql, params)

# create_one('123', 'cheng', '123')
# print(fetch_user('000'))