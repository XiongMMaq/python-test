#!/usr/local/bin/python3

'''
python3的迭代器与生成器
'''

#1、迭代器 iter() 和 next()。
list = [1,2,3,4,45]
it = iter(list)
print(next(it))
print(next(it))
#迭代器是一个可以记住遍历的位置的对象。
for x in it:
    print(x,end=',')


print("\n*****华丽分割线*****")

import sys
list1=[1,2,3,4]
it1 = iter(list1)    # 创建迭代器对象
 
while True:
    try:
        print (next(it1))
    except StopIteration:
        sys.exit()


#2、生成器 使用了 yield 的函数被称为生成器（generator）。

def fibonacci(n): # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n): 
            return
        yield a
        a, b = b, a + b
        counter += 1
f = fibonacci(10) # f 是一个迭代器，由生成器返回生成
 
while True:
    try:
        print (next(f), end=" ")
    except StopIteration:
        sys.exit()