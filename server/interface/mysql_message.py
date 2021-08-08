import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__)+'/'+'..'))
from database.pymysql_comm import UsingMysql
import ast

#----------------------------
# 添加接收信息列表
# 根据账号增加信息列表
def fetch_mes_by_filter(cursor, id):
    sql = f'select message from user where id = {id}' 
    cursor.execute(sql)
    data_str = cursor.fetchall()[0]['message']
    data_dict = ast.literal_eval(data_str)
    # print('-- 查询用户信息列表: %s'%data_dict)
    return data_dict
# 查找
def get_mes_by_id(id):
    with UsingMysql(log_time=False) as um:
        data_dict = fetch_mes_by_filter(um.cursor, id)
    #处理
    return data_dict

def up_mes_by_id(cursor, id, con):
    sql = f'''update user set message = "{con}" where id = {id}'''
    print(sql)
    cursor.execute(sql)

def update_mes_by_id(id, messages):
    with UsingMysql(log_time=False) as um:
                up_mes_by_id(um.cursor, id, messages)

# update_mes_by_id('234', "{'cheng': '今天天气怎么样？'}"), 
# print(type(get_mes_by_id(123)))