import requests
from bs4 import BeautifulSoup
# 이미지경로, 제목, 평점,등록일 추출
def saveImg(imgUrl,title):
    # print(imgUrl)
    # print(imgUrl[-4:])
    # print(title)
    title = title.replace(' :','')
    title = title.replace('(', '')
    title = title.replace(')', '')
    title = title.replace('/', '')
    filename='img\\'+title+imgUrl[-4:]
    print(filename)
    r = requests.get(imgUrl)
    with open(filename, 'wb') as f1:
        f1.write(r.content)

with open('data\\webtoon.csv','w',encoding='utf-8') as f:
    url='https://comic.naver.com/webtoon/list.nhn?titleId=733766&weekday=mon'
    recvd=requests.get(url)
    dom=BeautifulSoup(recvd.text,'lxml')
    table=dom.find('table',class_="viewList")
    trs=table.find_all('tr')
    for i in range(2,len(trs)):
        td=trs[i].find('td')
        img=td.find('img')['src']   #이미지경로
        # print(img)
        td1=trs[i].find('td',class_='title')
        title=td1.find('a').text
        saveImg(img,title)
        div=trs[i].find('div',class_="rating_type")
        rating=div.find('strong').text
        regdate=trs[i].find('td',class_="num").text
        f.write('{},{},{}\n'.format(title,rating,regdate))
