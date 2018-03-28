#!/usr/local/bin/python3
import request_model
util = request_model.RequestUtils("GET","http://cuiqingcai.com/")
print(util.getRequest())

print(util.postRequest())

print(util.jsonRequest())