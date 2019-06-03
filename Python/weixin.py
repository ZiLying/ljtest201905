import itchat
import requests
from itchat.content import *




@itchat.msg_register(TEXT)   
def simple_reply(msg):
    #这个是向发送者发送消息
    url = "http://open.turingapi.com/v1/openapi"
    data = {
        "input_text":msg['Text'],
        "user_info":{"open_id":"0bd6b605-3640-4178-813d-b3e18831c3f5"},
        "robot_id":"205436"
        }
    res = requests.post(url,json=data)
    res = res.json()
    redatas = res['result']['datas']
    for i in redatas:
        itchat.send_msg(i["value"],toUserName=msg['FromUserName'])
    # return "😄"     #返回的给对方的消息，msg["Text"]表示消息的内容


itchat.auto_login(hotReload=True)
itchat.run()


