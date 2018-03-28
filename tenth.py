#!/usr/local/bin/python3

#模块
import sys

print('命令行参数如下:')
for i in sys.argv:
   print(i)

print('\n\nPython 路径为：', sys.path, '\n')


#自定义模块与引入
import model_support

model_support.print_func("Tom")

model_support.fib(5)
print(model_support.fib2(5))