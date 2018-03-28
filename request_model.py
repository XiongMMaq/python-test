#!/usr/local/bin/python3

import requests
import urllib3
import json

class RequestUtils:
    #私有变量
    __privateVar = ""

    #公有变量
    method = ""
    url = ""

    #构造函数
    def __init__(self,method,url):
        print("RequestUtils的构造函数")
        self.method = method
        self.url = url

    #公有方法，（访问私有变量的方式）
    def visitPrivateVar(self):
        return self.__privateVar

    #私有方法，只能内部访问
    def __disableWarning__(self):
        requests.packages.urllib3.disable_warnings()

    #公有方法
    def getRequest(self):
        self.__disableWarning__()
        # 一个PoolManager实例来生成请求, 由该实例对象处理与线程池的连接以及线程安全的所有细节
        http = urllib3.PoolManager()
        # 通过request()方法创建一个请求：
        r = http.request(self.method, self.url)
        print(r.status) # 200
        return r.status
        # 获得html源码,utf-8解码
        #print(r.data.decode())
    
    #公有方法
    def postRequest(self):
        self.__disableWarning__()
        #你还可以通过request()方法向请求(request)中添加一些其他信息，如：
        header = {
             'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'
        }
        http = urllib3.PoolManager()
        r = http.request('POST','http://httpbin.org/post',fields={'hello':'world'},headers=header)
        print(r.data.decode())
        return r.data.decode

    #公有方法
    def jsonRequest(self):
        data={'attribute':'value'}
        encode_data= json.dumps(data).encode()
        http = urllib3.PoolManager()
        r = http.request('POST',
                            'http://httpbin.org/post',
                            body=encode_data,
                            headers={'Content-Type':'application/json'}
                        )
        print(r.data.decode('unicode_escape'))
        return r.data.decode('unicode_escape')
        

    