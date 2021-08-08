import os
import sys

from pymysql import NULL
sys.path.append(os.path.abspath(os.path.dirname(__file__)+'/'+'..'))
import interface.mysql_user as user
import interface.mysql_friends as friend
import interface.mysql_message as message

# async def login(id: str = None, pwd: str = None):
#     return { 'states': 1, 'username': '小明' }
class center :
    def __init__(self) -> None:
        pass
        
    def center_login(self, id: str = None, pwd: str = None):
        user_dict = user.fetch_user(id)
        res = { 'states': 0, 'username': '' }
        if user_dict == NULL:
            return res
        if user_dict['password'] == pwd:
            res['states'] = 1
            res['username'] = user_dict['name']
        return res 
    # print(center_login(123, '123'))

    # @app.get("/chat/regist")
    # async def regist(name: str = None, id: str = None, pwd: str = None):

    #     return {'states': 1}
    def center_regist(self, name: str = None, id: str = None, pwd: str = None):
        res = {'states': 1}
        user_dict = user.fetch_user(id)
        if user_dict != NULL:
            print("注册失败,账号已经存在")
            return {'states': 0}
        user.create_one(id, name, pwd)
        user_dict = user.fetch_user(id)
        if user_dict == NULL:
            print("注册失败")
            return {'states': 0}
        return res   
    # @app.get("/chat/get_fri_list")
    # async def get_fri_list(id: str = None, pwd: str = None):

    #     return {"friends": [{"id": "123456","name": "张三","online": 1},
    #                         {"id": "222226","name": "lisi","online": 1},
    #                         {"id": "1245","name": "xiap","online": 0},
    #                         ]}
                
    def center_get_fri_list(self, id: str = None, pwd: str = None):
        res = {"friends": []}
        if self.center_login(id, pwd)['states'] == 0:
            return res
        else:
            fri_list = friend.fetch_friend(id)
            
            tem = {"id": "","name": "","online": 0}
            
            for i in  fri_list:    
                info = user.fetch_user(i)
                tem['id'] = i
                tem['name'] = info['name']
                tem['online'] = info['state']
                res['friends'].append(tem)
                tem = tem.copy()
        print(res['friends'])
        return res

    # @app.get("/chat/send_mes")
    # async def send_mes(id: str = None, pwd: str = None, sendto: str = None, message: str = None):

    #     return {'states': 1}
    def center_send_mes(self, id: str = None, pwd: str = None, sendto: str = None, mess: str = None):
        if self.center_login(id, pwd)['states'] == 0:
            return {"states": 0}
        else:
            con = message.get_mes_by_id(sendto)
            
            con[id] = mess
            message.update_mes_by_id(sendto, str(con))
            return {"states": 1}
    # @app.get("/chat/get_mes")
    # async def get_mes(id: str = None, pwd: str = None, getto: str = None):
    #     return {'states': 1, 'message': 'hello'}
    def center_get_mes(self, id: str = None, pwd: str = None, getto: str = None):
        res = {'states': 0, 'message': ''}
        if self.center_login(id, pwd)['states'] == 0:
            return res
        else:
            tem = message.get_mes_by_id(id)
            if getto in tem.keys():
                res['message'] = tem[getto]
                res['states'] = 1  
                tem.pop(getto)
                message.update_mes_by_id (id, tem) 
            return res
            
    # @app.get("/chat/del_fri")
    # def del_fri(self, id, pwd, del_id):
    #     return {'states': 1}
    def center_del_add_fri(self, id, pwd, del_id):
        if self.center_login(id, pwd)['states'] == 0:
            
            return {'states': 0}
            
        else:
            if user.fetch_user(del_id) == NULL:
                 return {'states': 0}
            elif del_id == id:
                return {'states': 0}
            else :
                res = friend.delete_add_friend(id, del_id)
                friend.delete_add_friend(del_id, id)
                if res == 1:
                    print('添加成功')
                else :
                    print('删除成功')
                return {'states': 1}
   
    # # 获取留言信息
    # # 根据账号删除留言信息
    # @app.get("/chat/get_pub_mes") 
    # def get_pub_mes(id, pwd):
    #     return {'states': 1,'sender': '小红','mes': 'hhhhhh'}
    # print("欢迎使用聊天室")
    def center_get_pub_mes(self, id: str = None, pwd: str = None):
        res = {'states': 0,'sender': '','mes': ''}
        if self.center_login(id, pwd)['states'] == 0:
            return res
        else:
            tem = message.get_mes_by_id(id)
            if len(tem) == 0:
                return res
            else:
                sender = list(tem.keys())[0]
                res['states'] = 1  
                res['sender'] = user.fetch_user(sender)['name']
                res['mes'] = tem[sender]
                tem.pop(sender)
                message.update_mes_by_id (id, tem) 
            return res
      
a = center()
# a.center_regist('cheng', '234', '123')
# print(a.center_get_fri_list('1234','123'))
# print(type(message.get_mes_by_id('1234')))
# a.center_send_mes( '1234', '123', '234', '你好')
# print(message.get_mes_by_id('234'))
# print(a.get_pub_mes('234','123'))
# print(a.center_del_fri('1234','123','123'))