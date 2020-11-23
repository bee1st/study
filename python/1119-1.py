import requests
import json
with open('data\\sports.csv', 'w', encoding='utf-8') as f:
    # url = 'https://sports.news.naver.com/wfootball/news/index.nhn?isphoto=N'
    url = 'https://sports.news.naver.com/wfootball/news/list.nhn?isphoto=N'
    recvd = requests.get(url)
    # print(recvd)
    # print(recvd.text)
    dic = json.loads(recvd.text)
    print(dic)

    #기사제목, 내용을 출력
    # print(dic['list'])
    for i in dic['list']: #i = {}, {}, ..
        str = '*{}\n{}\n'.format(i['title'], i['subContent'])
        f.write(str)