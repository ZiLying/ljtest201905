# import time

# # rizhi = input("请输入今天的日志：")
# # now = time.strftime("%Y-%m-%d-%H-%M-%S")
# # print(now)
# with open("./日志.txt","r") as f:
#     aa = f.readlines()
# print(aa)
import requests
from dbtools import query

url = "http://127.0.0.1:5000/reg"
headers = {"Content-Type":"application/json"}
data = {"username":"testjjjj1511", "password":"test"}
res = requests.post(url,headers=headers,json=data)
res = res.json()
sql = "select * from t_user where username = '{}';".format(data["username"])
dbres = query(sql)
print(dbres)
if res["msg"] == True:
    if dbres[0][1] == data["username"]:
        print("测试通过，注册成功！")
    else:
        print("测试失败，数据没有正常的写入数据库")
else:
    print("测试失败！")
print(res)





