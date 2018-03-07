#!/usr/local/bin/python3

'''
@date create by xiongmingming in 2017-03-07
@description while循环例子

'''

n = 100
sum = 0
counter = 1
while counter <= n:
    sum += counter
    counter += 1
 
print("1 到 %d 之和为: %d" % (n,sum))




var = 1
while var == 1 :  # 表达式永远为 true
    try:
        num = int(input("输入一个数字  :"))
        print ("你输入的数字是: ", num)
    except ValueError:
        print("输入的字符串不能被转换成Int类型")
        break
print ("Good bye!")



# while...else...
count = 0
while count < 5:
   print (count, " 小于 5")
   count = count + 1
else:
   print (count, " 大于或等于 5")




## for 循环
sites = ["Baidu", "Google","Runoob","Taobao"]
for site in sites:
    if site == "Runoob":
        print("菜鸟教程!")
        break
    print("循环数据 " + site)
else:
    print("没有循环数据!")
print("完成循环!")


for i in range(5):
    print(i,end=',')
print("\n")

for i in range(2,10): #range指定区间的值
    print(i,end=',')
print("\n")

for i in range(2,10,3):#ange以指定数字开始并指定不同的增量(甚至可以是负数，有时这也叫做'步长'):
    print(i,end=',')
print("\n")

for i in range(-10, -100, -30) :
    print(i,end=",")


a = ['Google', 'Baidu', 'Runoob', 'Taobao', 'QQ']
for i in range(len(a))
    print(a[i],end=",") # print(i,a[i])

print(list(range(5)))


#break和continue语句及循环中的else子句
for letter in 'Runoob':     # 第一个实例
   if letter == 'b':
      break                 #break 语句可以跳出 for 和 while 的循环体。如果你从 for 或 while 循环中终止，任何对应的循环 else 块将不执行。
   print ('当前字母为 :', letter)
  
var = 10                    # 第二个实例
while var > 0:              
   print ('当期变量值为 :', var)
   var = var -1
   if var == 5:
      break
 
print ("Good bye!")



for letter in 'Runoob':     # 第一个实例
   if letter == 'o':        # 字母为 o 时跳过输出
      continue              #continue语句被用来告诉Python跳过当前循环块中的剩余语句，然后继续进行下一轮循环。
   print ('当前字母 :', letter)
 
var = 10                    # 第二个实例
while var > 0:              
   var = var -1
   if var == 5:             # 变量为 5 时跳过输出
      continue
   print ('当前变量值 :', var)
print ("Good bye!")


for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, '等于', x, '*', n//x)
            break
    else:
        # 循环中没有找到元素
        print(n, ' 是质数')


# pass 语句：Python pass是空语句，是为了保持程序结构的完整性。
while True:
    pass  # 等待键盘中断 (Ctrl+C)

class MyEmptyClass: #最小类
    pass

for letter in 'Runoob': 
   if letter == 'o':
      pass
      print ('执行 pass 块')
   print ('当前字母 :', letter)
 
print ("Good bye!")