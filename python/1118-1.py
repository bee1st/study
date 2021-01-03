# 영화제목 점수 (예매율), (상영시간)을 추출하여 data\\movie.csv저장
# 영화포스터는 img폴더에 저장
import requests
from bs4 import BeautifulSoup

def saveImg(imgUrl,title):
    filename='img\\' + title + imgUrl[-4:]
    print(filename)
    r = requests.get(imgUrl)
    with open(filename, 'wb') as f1:
        f1.write(r.content)

with open('data\\movie.csv','w',encoding='utf-8') as f:
    url = 'https://movie.naver.com/movie/running/current.nhn#'
    recvd = requests.get(url)
    dom = BeautifulSoup(recvd.text, 'lxml')
    table = dom.find('table', class_="viewList")
    trs = table.find_all('tr')
    for i in range(2,len(trs)):
        td=trs[i].find('td')
        img=td.find('img')['src']
        # print(img)
        td1=trs[i].find('td',class_='title')
        title=td1.find('a').text
        saveImg(img,title)
        div=trs[i].find('div',class_="rating_type")
        point =div.find('strong').text
        f.write('{},{}\n'.format(title,point))