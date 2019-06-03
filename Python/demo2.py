a = 1
b = 2
c = a + b
print(c)


b = 100
e = 22
f = b + e
print(f)


def jiafang(a,b):
    '''
    这是一个用来计算两个整数相加的方法
    '''
    if type(a) == int and type(b) == int:
        c = a + b
        print(c)
        return c
    else:
        print("请输入数字！")


def dayinhahah():
    print("哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈")



def digui(a):
    b = a/2
    if b > 10:
        digui(b)
    else:
        print(b)



def chulist(l):
    newl = []
    for i in l:
        if type(i) == int:
            newl.append(i)
    
    return newl



l = ["哈哈哈",123,"hhkdf",878,765,"gfsdgf"]
newl = chulist(l)
ic = 0
for i in newl:
    ic += i
print(ic)



# 包-->模块-->类-->方法-->变量


class GrilFriend:
    def __init__(self):
        self.age = 18
        self.high  = "165cm"
        self.weight = "50kg"
        self.yanzhi = "7fen"

    def zhufan(self,name):
        print("%s会煮饭哦~" % name)
    def nuanchuang(self):
        print("可以暖床哦~")
    def zhengqian(self):
        print("会挣钱养你哦~")
    

class NewGF(GrilFriend):
    def zhufan(self,name):
        print("%s会煮饭哦~，还会烧汤！！！" % name)


ngf = NewGF()
ngf.zhufan("黄爽")
ngf.nuanchuang()



name = "张三"



s = "你好，{name},{name}".format(name=name)
print(s)