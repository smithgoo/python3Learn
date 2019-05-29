#!/usr/bin/python
#coding:utf-8


import  requests

headers ={"user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36 QQBrowser/4.2.4763.400"}

response = requests.post("https://www.zhihu.com/question/21358581",headers =headers)

print(response.content)