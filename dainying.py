import urllib

import  re

url ='http://www.dytt8.net/html/gndy/dyzz/index.html'

response = urllib.urlopen(url).read()

# print(response)

req =r'<a href="(.*?)" class="ulink">(.*?)</a>'

listR = re.findall(req,response)

urlhost = 'www.dytt8.net'



def getUrl(listR):
    for urli in listR:
        url = urli[0];
        titil = urli[1];
        # print('%s'%titil.decode('gbk'));
        # print("%s" % (urlhost + url))
        geturlDetail(url)


def geturlDetail(url):
    responses = urllib.urlopen(url)
    print(responses)


if __name__ == '__main__':
    getUrl(listR)