# # 列表
# lst=['张三','李四','王五','迪丽热巴']
# lst1=lst
# # 查看列表中的数据
# print(lst)
#
# print(type(lst))
#
# name=lst[0]
# print(name)

#
# for i in range(4):
#     print(lst[i],end="  ")
# print('\n')
# print(len(lst))

# 列表的增删改查
# 增加
# lst.append('大黑子')
# print(lst)
# lst.insert(0,'李斯坦福')
# print(lst)

# 删除
# lst.pop()
# print(lst1)
# lst.remove('张三')
# print(lst1)
# lst1.clear()
# print(lst1)

# # 修改
# lst1[2]='hhahahah'
# print(lst1)

# 查找
# ret=lst1.index('李四')
# print(ret)

# # 售货机
# import time
# Goods = ['手机', '电脑', '鼠标', '平板']
# count=4
# print("售货机系统".center(30,'-'))
# while True:
#     print("剩下的商品为有")
#     for i in range(count):
#         print("商品序号:{0},名称：{1}".format(i + 1, Goods[i]))
#     ret = input("请输入需要购买的商品序号：(q/Q退出)>>>")
#     if ret.lower()=='q':
#         print("购买结束")
#         break
#     elif ret.isdigit():
#         if int(ret)>0 and int(ret)<=count:
#             IS=input("请问你购买的商品是："+Goods[int(ret)-1]+" (Y/N)>>>")
#             if IS.lower() == 'y':
#                 temp = int(ret) - 1
#                 print("-----------------购买中请稍后------------------")
#                 time.sleep(1)
#                 Goods.remove(Goods[temp])
#                 count = count - 1
#                 print("-------------------购买成功--------------------")
#             elif IS.lower() == 'n':
#                 print("您已取消购买该商品")
#             else:
#                 print("输入错误请重新输入")
#         elif count == 0:
#             print("亲，没货了！")
#             break
#         else:
#             print("该序号的商品不存在，请重新输入")
#     else:
#         print("该序号的商品不存在，请重新输入")


# 字典：用来保存事物的信息
user={'name':'张三','age':'18','gender':'男','height':'150'}

# (1)增加操作
# user['weight']=100

# (2)删除操作
# user.popitem()
# print(user)

# (3)修改操作
# user['age']=20
# print(user)

# (4)查找操作s
# name=user['name']
# print(name)
# age=user.get('ss',5)
# print(age)
# print(user)

# #列表里增加字典
# user_info_list=[
#      {'name':'张三','age':18,'sex':'男'},
#      {'name':'李四','age':20,'sex':'男'},
#      {'name':'王五','age':19,'sex':'男'},
#  ]
# for dic in user_info_list:
#     # print(dic)
#     name=dic['name']
#     print(name)


# 字典里增加列表
# dic_list_inof={'age':18,'sex':'男','user':['张三',20,'男']}
# ret=dic_list_inof['user'][2]
# print(ret)

# import time
# len=10
# print("开始加载".center(len,'-'))
# for i in range(len+1):
#     a = '*' * i
#     b = '.' * (len - i)
#     c = (i / len) * 100
#     time.sleep(0.1)
#     print("\r{0:3.0f}%[{1}{2}]".format(c, a, b),end='')
# print('\n')
# print("加载完成".center(len,'-'))


# 函数的作用：提高代码的重用率

"""
定义函数
"""
def say_hello():
    print("hello world@！")

"""
1.函数调用
"""
# say_hello()
# say_hello()
# say_hello()
# # 函数声明一次，可以调用多次

"""
2.python带参函数
"""
# def Add(a,b):
#     c = a+b
#     return c
# def FOR(a,b):
#     for i in range(a):
#         print(b)
#
# # C=Add('呵呵','hh')
# # print(C)
# FOR(5,'呵呵')

"""
3.默认参数
注意：带默认值得形式参数在函数定义的时候需要放在无默认值的形式参数后面
带默认值的形参，实参可以不输入。不带默认值的形参，实参必须输入
"""
def get_info(age=0, name='', gender='男'):
    print("该同学的信息是：")
    print("{}{:5}\t{}".format(name,age,gender))

# def get_info1(age, name='', gender='男'):
#     print("该同学的信息是：")
#     print("{}{:5}{}".format(name,age,gender.rjust(5)))
#
# # get_info(18,"如花","女")
# # get_info()
# get_info1(18,"胖大海","大佬")
# get_info(age=18,name='hh',gender="h")
# get_info(name='大海',age=18,gender="男")

"""
4.可变参数
"""
# *student 接受位置参数(以列表的形式寻找)
# **student1 接受关键字参数（以字典的形式寻找）

# def my_print(*student):
#     print(type(student))
#     print(student)
#     print(student[3])
# my_print("阿佛","奥斯卡","sdf",18)
# lst=["Sddsa","ssds","kosdkf"]
# print(type(lst))

# def my_print1(**student):
#     print(type(student))
#     print(student)
#     print(student["阿佛"])
#
# my_print1()


"""
练习题：用函数求n的阶乘
"""
# def fac(n):
#     SUM=1
#     for i in range(1,n+1):
#         SUM = SUM*i
#     return SUM
#
# valus=int(input("请输入一个数：>>>"))
# ret=fac(valus)
# print("该数的阶乘是：",ret)




"""
模块
"""
# 1.模块的导入方式有2种:
# 第一种方式：import 模块名称
# 第二种方式：from 模块名称 import 变量
import model模块         #导入整个模块
#调用model模块里的变量
print(model模块.name)
model模块.say_hello()

print("----------1---------")

from model模块 import name,say_hello   #导入模块里的变量
#调用model模块里的变量
print(name)
say_hello()

print("----------2---------")