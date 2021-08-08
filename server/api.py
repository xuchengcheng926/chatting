from fastapi import FastAPI
import uvicorn as uvicorn
from do.center import center

app = FastAPI()
do = center()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/chat/login")
async def login(id: str = None, pwd: str = None):

    return do.center_login(str(id), str(pwd))

@app.get("/chat/regist")
async def regist(name: str = None, id: str = None, pwd: str = None):

    return do.center_regist(str(name), str(id), str(pwd))

@app.get("/chat/get_fri_list")
async def get_fri_list(id: str = None, pwd: str = None):

    return do.center_get_fri_list(str(id), str(pwd))
            
            
@app.get("/chat/send_mes")
async def send_mes(id: str = None, pwd: str = None, sendto: str = None, message: str = None):

    # return {'states': 1}
    return do.center_send_mes(str(id), str(pwd), str(sendto), str(message))

@app.get("/chat/get_mes")
async def get_mes(id: str = None, pwd: str = None, getto: str = None):

    return do.center_get_mes(str(id), str(pwd), str(getto))

@app.get("/chat/del_fri")
def del_fri(id, pwd, del_id):
    print('--------------'+str(del_id))
    return do.center_del_add_fri(str(id), str(pwd), str(del_id))

@app.get("/chat/add_fri")
def add_fri(id, pwd, add_id):
    
    return do.center_del_add_fri(str(id), str(pwd), str(add_id))

# 获取留言信息
# 根据账号删除留言信息
@app.get("/chat/get_pub_mes") 
def get_pub_mes(id, pwd):
    return do.center_get_pub_mes(str(id), str(pwd))

if __name__ == '__main__':
    uvicorn.run(app='api:app', host="ddns.chengs.tk", port=8000, reload = True)
