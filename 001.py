import requests

from retrying   import retry

@retry(stop_max_attempt_number =3)

def _parse_url(url):
    print("***"*100)
    respond  = requests.get(url)
    return respond.content.decode()



def parse_url(url):
    try:
        html_str = _parse_url(url)
    except:
        html_str = None

    return  html_str

if __name__ == '__main__':
    url = "http://www.baidu.com"
    print(parse_url(url)[:100])