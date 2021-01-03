import requests
from bs4 import BeautifulSoup
with open('data\\kma.csv', 'w', encoding = 'utf-8') as f:
    url='http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108'
    recvd = requests.get(url)
    # print(recvd.text)
    # print(recvd)
    # 서울 인천 경기도 서울 기상 데이터
    dom = BeautifulSoup(recvd.text, 'lxml')
    locations = dom.find_all('location')
    # print(len(locations))
    for location in locations:
        province = location.find('province')
        city = location.find('city')
        # print(province, city)
        datas = location.find_all('data')
        for data in datas:
            mode=data.find('mode').text
            tmef=data.find('tmef').text
            wf=data.find('wf').text
            tmn=data.find('tmn').text
            tmx=data.find('tmx').text
            reliability = data.find('reliability').text
            rnst = data.find('rnst').text
            str = '{}, {}, {}, {}, {}, {}, {}, {}, {}\n'.format(province, city, mode, tmef, wf, tmn, tmx, reliability, rnst)
            print(str)
            f.write(str)

