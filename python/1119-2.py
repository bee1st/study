import json
import requests
from fake_useragent import UserAgent
with open('data\\money.csv', 'w', encoding='utf-8') as f:
    ua = UserAgent() # UserAgent ua = new UserAgent();
    # print(ua.chrome)
    print(ua.ie)
    headers = {'user-agent' : ua.chrome, 'referer' : 'https://finance.daum.net/'}
    url = 'http://finance.daum.net/api/search/ranks?limit=10'
    recvd = requests.get(url, headers = headers)
    dic = json.loads(recvd.text)
    # print(dic)
    for i in dic['data']: #i = {}, {}, ..
            str = '{}. {} {}\n'.format(i['rank'], i['name'], i['tradePrice'])
            f.write(str)

