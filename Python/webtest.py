from selenium import webdriver
import time
# 对浏览器进行实例化
driver = webdriver.Chrome(executable_path="./chromedriver")
# 打开对于的网站
time.sleep(5)
driver.get("http://118.24.29.59:8080")
# time.sleep(5)
driver.find_element_by_id("J_header_lnkLogin").click()
time.sleep(3)
# phonenum = "18112340987"
# driver.find_element_by_id("username").send_keys(phonenum)
# driver.find_element_by_id("getCode").click()
# password = "123456aA"
# driver.find_element_by_id("password").send_keys(password)
# driver.find_element_by_id("rePassword").send_keys(password)
# time.sleep(4)
# driver.find_element_by_id("btnReg").click()
# time.sleep(5)
# 关闭浏览器
phonenum = "18112340987"
password = "123456aA"
driver.find_element_by_id("username").send_keys(phonenum)
driver.find_element_by_id("password").send_keys(password)
# time.sleep(5)
driver.find_element_by_id("btnLogin").click()

text = driver.find_element_by_id("J_head_log").text
print(text)
if phonenum in text:
    print("登陆成功！！！测试通过！！！")
else:
    print("登陆异常，测试失败！！！！")
time.sleep(5)
driver.quit()

