#!/usr/local/bin/python3

flag = 0
print(not flag)
flag = 1
print(not flag)


import os,sys

if __name__=="__main__":

    #当前文件的路径
    print("__file__ : {}".format(__file__))
    #当前文件的目录
    print("os.path.dirname(os.path.realpath(__file__)) : {}".format(os.path.dirname(os.path.realpath(__file__))))
    #当前文件的目录
    print("os.path.split(os.path.realpath(__file__)) : {}".format(os.path.split(os.path.realpath(__file__))[0]))