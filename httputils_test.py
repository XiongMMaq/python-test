#!/usr/local/bin/python3

import httputils
import json

url = 'https://usop.10101111.com/utree_api/server_details/'
fields = {'user':'framework','token':'4jj-53048368eac0f4fdf988','ip_list':'[\"10.204.247.220\", \"10.204.247.208\"]'}

utils = httputils.HttpUtils('POST',url,fields)
print(utils.doPost())