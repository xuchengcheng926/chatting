import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__)+'/'+'..'))
from database.pymysql_comm import UsingMysql

#----------------------------
# 查询用户好友列表 
# 根据账号获取好友列表
def fetch_friend_by_filter(cursor, id):
    sql = f'select friends from user where id = {id}' 
    cursor.execute(sql)
    data_list = cursor.fetchall()[0]['friends'].split('%')[:-1]
    # print('-- 查询用户好友列表: %s'%data_list)
    return data_list
# 查找
def fetch_friend(id):
    with UsingMysql(log_time=False) as um:
        data_list = fetch_friend_by_filter(um.cursor, id)
    return data_list


#----------------------------
# 删除用户好友列表
# 根据账号删除好友列表
# 增加用户好友列表
# 根据账号增加好友列表
def update_fri_by_id(cursor, id, con):
    sql = f'''update user set friends = "{con}" where id = {id}'''
    print(sql)
    cursor.execute(sql)
def con_update(res, index, friend_id = 0):
    con = ''
    for i in range(len(res)):
        if i == index:
            continue
        con = con + res[i] + '%'
    if index == -1 :
        con = con + friend_id + '%'
    return con
#有该好友则删除该好友返回0
#没有该好友则添加好友返回1
def delete_add_friend(id, friend_id):
    res = fetch_friend(str(id))
    for i in range(len(res)):
        if res[i] == friend_id:
            with UsingMysql(log_time=False) as um:
                data_list = update_fri_by_id(um.cursor, id, con_update(res, i))
                return 0
    with UsingMysql(log_time=False) as um:
                data_list = update_fri_by_id(um.cursor, id, con_update(res, -1, friend_id))
    return 1      
        

# print(fetch_friend('1234'))
