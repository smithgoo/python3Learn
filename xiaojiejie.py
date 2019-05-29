# coding: utf -8

from  bs4 import BeautifulSoup

import  urllib

import  requests


def getUrl():

    response = urllib.urlopen('http://www.meizitu.com/a/legs.html')
    response.encoding ='gb2312'
    # html = response.text

    # print(html)

    supe =BeautifulSoup(html)

    print(type(supe))

    girl = supe.find_all('img')

    for i in girl:
        link = i.get('src')
        name = i.get('alt')
        print(type(name))
        print("正在下载%s"%name)

        urllib.urlretrieve(link,'img\%s.jpg'%name)






if __name__ == '__main__':
    getUrl()
