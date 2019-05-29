import  urllib
import re
from lxml import etree
import requests
#
# req =r'<a href="(.*?)">(.*?)</a>'
#
#
# result =re.findall(req,response)
#
# for url in  result:
#
#     itemurl =url[0]
#     itemtitle =url[1]
#     print(itemurl,itemtitle)






headers ={"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1","Referer": "http://fanyi.baidu.com/translate?aldtype=16047&query=&keyfrom=baidu&smartresult=dict&lang=auto2zh"}

# for url in  result:
#
#     itemUrl ="http://www.dytt8.net/"+url
#     seResponse = urllib.urlopen(itemUrl).read()
#     seResponse =seResponse.decode('gbk')
#     seElement = etree.HTML(seResponse)
#     seResult =element.xpath("//a[@href='#']/@thunderrestitle")
#     print(seResponse)

# print(result)

def getthirthUrlStr(url):
    # response = urllib.urlopen(url).read()
    response = requests.get(url,headers =headers)
    # response = response.decode('gbk')

    # print(response)
    element = etree.HTML(response.content.decode('gbk'))
    result = element.xpath('//*[@id ="Zoom"]/span/table/tbody/tr/td/a')

    print(result)

    # return  result.text



def getSecondUrlStr(urlList):
    for urls in urlList:
        url = 'http://www.dytt8.net'+urls
        print(url)
        getthirthUrlStr(url)


def getFirstUrlStr():
    url = 'http://www.dytt8.net/html/gndy/dyzz/index.html'
    response = urllib.urlopen(url).read()
    response = response.decode('gbk')
    element = etree.HTML(response)
    result = element.xpath("//div[@class='co_content8']//a/@href")
    getSecondUrlStr(result)

if __name__ == '__main__':
    str =getthirthUrlStr("http://www.dytt8.net/html/gndy/dyzz/20180808/57259.html")
    print(str)
