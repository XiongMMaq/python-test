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
print(isinstance(a,int))

var_a = 1 #当你指定一个值时，Number 对象就会被创建
var_b = 3

del var_a #del语句删除单个或多个对象 del var_a,var_b

#print(var_a)
print(var_b)

#3.2、isinstance与type的区别
#type()不会认为子类是一种父类类型。
#isinstance()会认为子类是一种父类类型。
class A:
    pass
class B(A):
    pass
isinstance(A(), A)  # returns True
type(A()) == A      # returns True
isinstance(B(), A)    # returns True
type(B()) == A        # returns False

#3.3、数值运算
print(5 + 4) #求和
print(4.3 - 2) #减法
print(3 * 7) #乘法
print(2 / 4) #除法，得到的是浮点数
print(2 // 4) #除法，得到的是整数
print(17 % 3) #取余
print(2 ** 5) #乘方

var_a,var_b = 3,4 #同时赋值
print(var_a,var_b)


#3.3、String（字符串）：Python中的字符串用单引号(')或双引号(")括起来，同时使用反斜杠(\)转义特殊字符。
#注意：python的字符串一旦创建，不能改变
str = 'Runoob'
 
print (str)          # 输出字符串
print (str[0:-1])    # 输出第一个到倒数第二个的所有字符
print (str[0])       # 输出字符串第一个字符
print (str[2:5])     # 输出从第三个开始到第五个的字符
print (str[2:])      # 输出从第三个开始的后的所有字符
print (str * 2)      # 输出字符串两次
print (str + "TEST") # 连接字符串

print('Ru\noob') #使用反斜杠(\)转义特殊字符，
print(r'Ru\noob') #如果你不想让反斜杠发生转义，可以在字符串前面添加一个 r，表示原始字符串：

word = 'Python' #Python中的字符串有两种索引方式，从左往右以0开始，从右往左以-1开始。
print(word[0], word[5])
print(word[-1], word[-6])

str1 = '''asdasf 
        daasfasdf'''
print(str1) #使用 """...""" 或者 '''...''' 跨越多行


#3.4、List（列表）：List写在方括号之间，元素用逗号隔开。 Python 中使用最频繁的数据类型，索引值以 0 为开始值，-1 为从末尾的开始位置。
list = [ 'abcd', 786 , 2.23, 'runoob', 70.2 ]
tinylist = [123, 'runoob']
 
print (list)            # 输出完整列表
print (list[0])         # 输出列表第一个元素
print (list[1:3])       # 从第二个开始输出到第三个元素
print (list[2:])        # 输出从第三个元素开始的所有元素
print (tinylist * 2)    # 输出两次列表
print (list + tinylist) # 连接列表


a = [1, 2, 3, 4, 5, 6] #Python字符串不一样的是，列表中的元素是可以改变的：
a[0] = 9 #第一个元素改成9
a[2:5] = [13, 14, 15] #第三个元素往后修改为新的数字
print(a)
a[2:5] = []   # 将对应的元素值设置为 []
print(a)

#3.5、Tuple（元组）：元组写在小括号(())里，元素之间用逗号隔开。元组的元素是不能修改的

tup1 = ()    # 空元组
tup2 = (20,) # 一个元素，需要在元素后添加逗号

tuple = ( 'abcd', 786 , 2.23, 'runoob', 70.2  )
tinytuple = (123, 'runoob')
 
print (tuple)             # 输出完整元组
print (tuple[0])          # 输出元组的第一个元素
print (tuple[1:3])        # 输出从第二个元素开始到第三个元素
print (tuple[2:])         # 输出从第三个元素开始的所有元素
print (tinytuple * 2)     # 输出两次元组
print (tuple + tinytuple) # 连接元组

#tuple[0] = 11 # 修改元组元素的操作是非法的

#print(tuple)

#3.6、Set（集合）：集合（set）是一个无序不重复元素的序列。基本功能是进行成员关系测试和删除重复元素。
#可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。

student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}

print(student)   # 输出集合，重复的元素被自动去掉

# 成员测试
if('Rose' in student) :
    print('Rose 在集合中')
else :
    print('Rose 不在集合中')
 
 
# set可以进行集合运算
a = set('abracadabra')
b = set('alacazam')

print(a)
print(b - a)     # b与a的差集
print(a - b)     # a和b的差集
print(a | b)     # a和b的并集
print(a & b)     # a和b的交集
print(a ^ b)     # a和b中不同时存在的元素


#3.7、Dictionary（字典）:字典（dictionary）是Python中另一个非常有用的内置数据类型。
#字典是一种映射类型，字典用"{ }"标识，它是一个无序的键(key) : 值(value)对集合。键(key)必须使用不可变类型。
#在同一个字典中，键(key)必须是唯一的。
dict = {}
dict['one'] = "1 - 菜鸟教程"
dict[2]     = "2 - 菜鸟工具"

tinydict = {'name': 'runoob','code':1, 'site': 'www.runoob.com'}
 
print (dict)
print (dict['one'])       # 输出键为 'one' 的值
print (dict[2])           # 输出键为 2 的值
print (tinydict)          # 输出完整的字典
print (tinydict.keys())   # 输出所有键
print (tinydict.values()) # 输出所有值



