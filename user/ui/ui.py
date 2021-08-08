import os
from interface.api import api
import _thread
import time

class ui:

    def __init__(self) :
        self.server = api()
        self.MY_ID = 0
        self.MY_PWD = 0
        self.MY_NAME = ''
        self.DELAY = 0.5
        self.chatting_flag = 0
        self.pub_rec_statue = 0 #是否接收公共频道信息
        pass
    
    def receive_mes(self, friend):
        while self.chatting_flag:
            res = self.server.get_mes(self.MY_ID, self.MY_PWD, friend[0])
            if res[0] == 1 :
                print("{}: ".format(friend[1])+res[1])
            time.sleep(self.DELAY)

    def rec_pub_mes(self):
        time.sleep(4)
        while 1 :
            if self.pub_rec_statue ==1 :
                res = self.server.get_pub_mes(self.MY_ID, self.MY_PWD)
                if res[0] == 1 :
                    print("{}: ".format(res[1])+res[2])
            time.sleep(self.DELAY)

    def send_mes(self, friend, message):
        res = self.server.send_mes(self.MY_ID, self.MY_PWD, friend[0], message)
        if res == 1 :
            print("{}: ".format(self.MY_NAME)+message)
        else :
            print("发送出错")
        

    def chatwith(self, friend):
        print("正在进入聊天室...")
        print("输入exist退出聊天")
        self.chatting_flag = 1
        self.pub_rec_statue = 0 #进入到私人聊天室，暂时关闭公共频道信息
        # 创建两个线程
        try:
            _thread.start_new_thread(self.receive_mes, (friend, ))
        except:
            print("Error: unable to start thread")

        while True:
            message =input()
            if message =='exist':
                self.chatting_flag = 0
                break
            else:
                self.send_mes(friend, message)
        os.system("clear")
        self.pub_rec_statue = 1 #退出私人聊天室，开启共频道信息
        self.menu()
        
        
        

    def display_friends(self):
        friedns = self.server.get_fri_list(self.MY_ID, self.MY_PWD)
        print("好友列表")
        i = 0
        for friend in friedns:
            if friend[2] ==1:
                statue = "在线"
            else :
                statue = "离线"
            id = friend[0]
            name = friend[1]
            i = i+1
            print('{:<{len}}'.format(i, len=5)+'{:<{len}}'.format(id, len=10)+'[{name:<{len}}\t'.format(name=name+']',len=15-len(name.encode('GBK'))+len(name))+statue)
        return friedns
        

    def chatting(self):
        fri_list = self.display_friends()
        print('\n')
        print("请输入想聊天的好友,按0返回菜单")
        num = input()
        if num == '0' :
            os.system("clear")
            self.menu()
        else:
            os.system("clear")
            if int(num) > len(fri_list) or int(num) < 0:
                self.chatting()
            else:
                self.chatwith(fri_list[int(num)-1])
        
        

    def add_rm_friends(self):
        fri_list = self.display_friends()
        print("\n")

        print("请输入你要删除/添加好友的ID")
        res = input()
        flag = 0
        for friend in fri_list:
            if friend[0] == res: 
                flag = 1
        if flag == 1:
            if self.server.del_fri(self.MY_ID, self.MY_PWD, res) == 1:
                print("删除好友成功")
            else :
                print("删除失败！")
        else:
            if self.server.add_fri(self.MY_ID, self.MY_PWD, res) == 1:
                print("添加好友成功")
            else :
                print("添加好友失败")
        time.sleep(1)
        os.system("clear")
        self.menu()
        
    def menu(self):
        fri_list = self.display_friends()
        print("\n")
        print("菜单")
        print("1-私人聊天")
        print("2-添加/删除好友")
        print("3-退出软件")

        
        tem = input()
        
        if tem == '1':
            os.system("clear")
            self.chatting()
        elif tem == '2':
            os.system("clear")
            self.add_rm_friends()
        else :
            os.system("clear")
            exit(0)
        
        

    def login(self):
        print("请输入账号")
        id = input()
        print("请输入密码")
        pwd = input()
        print("正在登陆...")
        print("\n")
        # print("id is: "+id+" pwd is: "+pwd)
        res = self.server.login(id, pwd)
        if res[0] == 1 :
            os.system("clear")
            self.MY_ID = id
            self.MY_PWD = pwd
            self.MY_NAME = res[1]
            self.pub_rec_statue = 1
            try:
                _thread.start_new_thread(self.rec_pub_mes, ( ))
            except:
                print("Error: unable to start thread")
                exit(0)
            self.menu()
        else :
            print("账号密码出错")
            time.sleep(2)
            os.system("clear")
            self.welcome()
        

    def register(self):
        print("请输想注册的入账号名称 例如：小明、123、hh8")
        name = input()
        print("请输想注册的入账号id id为5位长数字 例如：12345")
        id = input()
        print("请设置密码 密码长度小于5位，为数字或字母组合 例如：it34f、1、234")
        pwd = input()
        print("请再次确认密码")
        pwd2 = input()
        print("正在注册...")
        if pwd == pwd2:
            print("\n")
            # print("name"+name+"id"+id+"pwd"+pwd)
            #注册函数
            res = self.server.regist(name, id, pwd)
            if res == 1:
                print('注册成功')
            else:
                print('注册失败')
            time.sleep(2)
            os.system("clear")
            self.welcome()
        else :
            print("注册失败，请保证两次密码相同\n")
            os.system("clear")
            self.register()
        

    def welcome(self):
        print("欢迎使用chengs的聊天程序\n")
        print("请选择")
        print("1-我有账号，登录")
        print("2-我没有账号，需要注册")
        tem = input()
        if tem == '1':
            os.system("clear")
            self.login()
        elif tem == '2':
            os.system("clear")
            self.register()
        else:
            print("请选择正确选项")
            self.welcome()
        
