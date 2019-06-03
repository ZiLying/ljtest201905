
import itchat
from itchat.content import *
import requests


@itchat.msg_register(TEXT)
def remsg(msg):
    print(msg["User"]["NickName"],"说：",msg["Text"])
    url = "http://open.turingapi.com/v1/openapi"
    payload = {"input_text":msg["Text"],"user_info":{"open_id":"0bd6b605-3640-4178-813d-b3e18831c3f5"},"robot_id":"205436"}
    headers = {
        'Content-Type': "application/json"
        }
    response = requests.request("POST", url, json=payload, headers=headers)
    res = response.json()
    datas = res["result"]["datas"]
    for i in datas:
        print("我回答：",i["value"])
        itchat.send_msg(i["value"],toUserName=msg['FromUserName'])


itchat.auto_login(hotReload=True)
itchat.run()



