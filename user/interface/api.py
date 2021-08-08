import requests
import json
class api:
    def __init__(self) -> None:
        self.URL = "http://ddns.chengs.tk:8000/chat/"
        pass
    def cilent_get (self, sub_url, data) :
        url = self.URL+str(sub_url)
        #将要传的参数以key value的形式定义在data字典中
        try:
            responds = requests.get(url=url,
                        params=data)
            res = json.loads(responds.text)
        except:
                print("Error: unable to connect")
                exit(0)
        return res

    def login (self, id, pwd):
        if len(id) != 5 :
            return [0]
        elif len(pwd) >5:
            return [0]

        data = {"id":str(id),"pwd":str(pwd)}
        responds = self.cilent_get('login', data)

        res = list(responds.values())
        return res
    def regist (self, name, id, pwd):
        if len(id) != 5 :
            return 0
        elif len(pwd) >5:
            return 0
        
        data = {"name": str(name), "id":str(id),"pwd":str(pwd)}
        print(data)
        responds = self.cilent_get('regist', data)

        res = list(responds.values())[0]
        return res
    def get_fri_list(self, id, pwd):
        
        #将要传的参数以key value的形式定义在data字典中
        data = {"id":str(id),"pwd":str(pwd)}
        
        responds = self.cilent_get("get_fri_list", data)

        res = list(responds.values())[0]
        lists =[]
        for i in res:
            lists = lists + [list(i.values())]
        return lists
    def send_mes(self, id, pwd, sendto, message):
        data = {"id":str(id),"pwd":str(pwd), "sendto": str(sendto), "message": str(message)}
        responds = self.cilent_get('send_mes', data)

        res = list(responds.values())[0]
        return res
    def get_mes(self, id, pwd, getto):
        data = {"id":str(id),"pwd":str(pwd), "getto": str(getto)}
        responds = self.cilent_get('get_mes', data)

        res = list(responds.values())
        return res
    def del_fri(self, id, pwd, del_id):
        data = {"id":str(id),"pwd":str(pwd), "del_id": str(del_id)}
        responds = self.cilent_get('del_fri', data)

        res = list(responds.values())[0]
        return res
    def add_fri(self, id, pwd, add_id):
        data = {"id":str(id),"pwd":str(pwd), "add_id": str(add_id)}
        responds = self.cilent_get('add_fri', data)

        res = list(responds.values())[0]
        return res
    def get_pub_mes(self, id, pwd):
        data = {"id":str(id),"pwd":str(pwd)}
        responds = self.cilent_get('get_pub_mes', data)

        res = list(responds.values())
        return res

# i = api()
# # res = list(res.values())
# print(i.get_pub_mes('xx','id'))