#!/usr/local/bin/python3
#1、内置函数

#1.1、eval()
x = 7
print(eval( '3 * x' ))
print(eval('pow(2,4)')) #求2的4次方
print(eval('2+2'))


#1.2、tuple()
list1= ['Google', 'Taobao', 'Runoob', 'Baidu']
tuple1=tuple(list1) #list转tuple
print(tuple1) 


#1.3、list()
aTuple = (123, 'Google', 'Runoob', 'Taobao')
list1 = list(aTuple) #tuple 转 list
print ("列表元素 : ", list1)

str="Hello World"
list2=list(str) #String 转 list
print ("列表元素 : ", list2)

#1.4、set():set() 函数创建一个无序不重复元素集，可进行关系测试，删除重复数据，还可以计算交集、差集、并集等。

#1.5、dict()
list = [('one', 1), ('two', 2), ('three', 3)]
print(dict(list)) # # 可迭代对象方式来构造字典. list 转 dict

print(dict(zip(['one', 'two', 'three'], [1, 2, 3]))) ## 映射函数方式来构造字典

print(dict(a='a', b='b', t='t'))     # 传入关键字

#1.6、frozenset() 转换为不可变集合
a = frozenset(range(10))  # 生成一个新的不可变集合
print(a)

b = frozenset('runoob') 
print(b)

#1.7、chr()将一个整数转换为一个字符
print (chr(0x30), chr(0x31), chr(0x61))   # 十六进制
print (chr(48), chr(49), chr(97))         # 十进制

#1.8、ord()将一个字符转换为它的整数值
print(ord('a'),ord('b'),ord('c'))

#1.9、hex() 函数用于将10进制整数转换成16进制，以字符串形式表示。

print(hex(255),hex(-42),hex(1),hex(12))
print(type(hex(12)))

#1.10、oct()将一个整数转换为一个八进制字符串
print(oct(10))
print(oct(20))
print(oct(15))