#!/usr/local/bin/python3

import urllib3
import json

class HttpUtils:

    method = ""
    url = ""
    fields = ""

    def __init__(self,method,url,fields):
        self.method = method
        self.url = url
        self.fields = fields

    #form-data 方式提交数据
    def doPostFormData(self):
        http = urllib3.PoolManager()
        response = http.request(self.method,self.url,fields=self.fields)
        result = json.loads(response.data.decode('utf-8'))
        return result
