#!/usr/local/bin/python3

import json

# 1.1、Python 字典类型转换为 JSON 对象
data1 = {
    'no' : 1,
    'name' : 'Runoob',
    'url' : 'http://www.runoob.com'
}

json_str = json.dumps(data1)
print ("Python 原始数据：", repr(data1))
print ("JSON 对象：", json_str)

# 1.2、将 JSON 对象转换为 Python 字典
data2 = json.loads(json_str)
print ("data2['name']: ", data2['name'])
print ("data2['url']: ", data2['url'])


print("*************华丽分割线**************")


data = {
    'age' : 12,
    'name' : 'XiongMM'
}

# 2.1、写入 JSON 数据
with open('./python-test/json_data.json', 'w') as f:
    json.dump(data, f)

# 2.2、读取数据
with open('./python-test/json_data.json', 'r') as f:
    newdata = json.load(f)
    print("json_data的数据为：{}".format(repr(newdata)))