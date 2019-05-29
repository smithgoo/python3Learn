# coding: utf -8

import urllib.request

import re

def getNoverContent():

    html = urllib.request.urlopen('http://www.quanshuwang.com/book/44/44683').read()

    html = html.decode('gbk')

    # print(html)

    req = r'<li><a href="(.*?)" title=".*?">(.*?)</a></li>'

    urls = re.findall(req, html)


    # print(urls)

    for url in  urls:

        nover_url = url[0]

        nover_title = url[1]

        chapt = urllib.request.urlopen(nover_url).read()

        chaptHtml = chapt.decode('gbk')
        # print(chapt)

        req = r'</script>&nbsp;&nbsp;&nbsp;&nbsp;(.*?)<script type="text/javascript">'

        req = re.compile(req,re.S)

        chapt_content = re.findall(req,chaptHtml)

        # print(chapt_content[0])

        simpleStr = chapt_content[0].replace('&nbsp;&nbsp;&nbsp;&nbsp;','')

        

        simpleStr = simpleStr.replace('<br />','')
        # print(simpleStr)

        print(u'正在保存%s' % nover_title)

        # f =  open(u'{}.text'.format(nover_title),'w')
        # print(type(simpleStr))
        # print(simpleStr)
        # f.write(simpleStr.encode('utf-8'))
        #
        # f.close()
        # print(nover_title)


        with open('{}.text'.format(nover_title),'w') as f:

            f.write(simpleStr)



if __name__ == '__main__':
    getNoverContent()
