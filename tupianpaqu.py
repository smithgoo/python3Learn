import requests
import re
import urllib
from lxml import  etree
from bs4 import BeautifulSoup

headers ={"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1","Referer": "http://fanyi.baidu.com/translate?aldtype=16047&query=&keyfrom=baidu&smartresult=dict&lang=auto2zh"}

url ='http://www.meizitu.com/a/legs.html'

html = urllib.urlopen(url).read()

html = html.decode('gbk')


# element = etree.HTML(response.content)
# result = element.xpath("//div[@class='pic']/a//@src")
# titles = element.xpath("//div[@class='pic']/a/img/@alt")
req =r'<img src="(.*?)" alt="(.*?)">'

result = re.findall(req,html)

for res in result:
    mainurl =res[0]
    maintitle =res[1]

    print(mainurl,maintitle)

    f = open(u'{}.jpg'.format(maintitle[5]), 'w')
    print(type(mainurl))
    f.write(mainurl)

    f.close()
    print(maintitle[5])



