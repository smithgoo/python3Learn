#!/usr/bin/python
#coding:utf-8

import  requests
import json

headers ={"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1","Referer": "http://fanyi.baidu.com/translate?aldtype=16047&query=&keyfrom=baidu&smartresult=dict&lang=auto2zh"}


url = "http://fanyi.baidu.com/basetrans"

words = raw_input("中翻英:")

requestdic ={"query":words,"from":"en","to":"zh"}


response = requests.post(url,data=requestdic,headers =headers)

# response.encoding = "utf-8"

print(response)

print(response.content.decode())

htmlstr = response.content.decode()

str1 = json.loads(htmlstr)

print(str1)

print(type(str1))

str2 = str1["trans"][0]["dst"]

print(str2)
