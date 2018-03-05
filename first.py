#!/usr/local/bin/python3
import keyword

# 1、判断
if True:
    print("xxx")
    print("yyy")
    #2、循环
    for i in range(1,7):
        print(i)
else:
    pass
item_one = "1"
item_two = "2"
item_three = "3"

#3、换行继续写
total = item_one + \
        item_two + \
        item_three
print("halou" + total)

#4、字符串,单字符串，双字符串和三字符串
word = '字符串'
sentence = "这是一个句子。"
paragraph = """这是一个段落，
可以由多行组成"""
paragraph2 = '''这是一个段落，
可以由多行组成'''
print(word)
print(sentence)
print(paragraph) 
print(paragraph2)

#5、等待输入nihao
#xx = input("\n\n按下 enter 键后退出。")
#print(xx)

#6、数据类型（int long float complex）
x_one = 6
print(x_one * 2)

x_two = 7.3
print(x_two * 4.3)

#7、同一行显示多条语句
import sys; x = 'runoob'; sys.stdout.write(x + '\n')

#8、sys
import sys
print('================Python import mode==========================');
print ('命令行参数为:')
for i in sys.argv:
    print (i)
print ('\n python 路径为',sys.path)


#9、function
def example(anything):
    xx_one = '''形参为任意类型的对象，
       这个示例函数会将其原样返回。
    '''
    return xx_one

print(example("nihao"))