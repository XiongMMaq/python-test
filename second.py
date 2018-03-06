#!/usr/local/bin/python3
#1、基本数据类型
counter = 100          # 整型变量
miles   = 1000.0       # 浮点型变量
name    = "runoob"     # 字符串
 
print (counter)
print (miles)
print (name)

#2、多变量赋值
a = b = c = 1
print(a)
print(b)
print(c)

a, b, c = 1, 2, "runoob"
print(a)
print(b)
print(c)

#3、标准数据类型
#3.1、Number(数字)：Python3 支持 int、float、bool、complex（复数）。
a, b, c, d = 20, 5.5, True, 4+3j
print(type(a),type(b),type(c),type(d))
