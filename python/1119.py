import requests
from bs4 import BeautifulSoup
import os
def saveImg(imgUrl, title):
    # print(imgUrl)
    # print(len(imgUrl))
    # print(imgUrl.index('?'))
    # print(imgUrl[:83])
    # print(imgUrl[79:83])
    # print(imgUrl[imgUrl.index('?')-4:imgUrl.index('?')])
    title = title.replace(':', '')
    filename = 'img\\' + title + imgUrl[imgUrl.index('?')-4:imgUrl.index('?')]
    print(filename)
    r = requests.get(imgUrl)
    with open(filename, 'wb') as f1:
        f1.write(r.content)

with open (os.path.join('data', 'movies.csv'), 'w', encoding='utf-8') as f:
    url='https://movie.naver.com/movie/running/current.nhn'
    recvd = requests.get(url) #get방식 url을 recvd 변수에 저장
    dom = BeautifulSoup(recvd.text, 'lxml')
    ul = dom.find('ul', class_ = "lst_detail_t1") 
    lis = ul.find_all('li')
    for li in lis:
        img=li.find('img')['src']
        title=li.find('dt',class_ ="tit").find('a').text
        saveImg(img,title)
        rating=li.find('span',class_="num").text
        reserv=li.find('div', class_="star_t1 b_star")
        if reserv==None :
            temp = ''
        else:
            temp=reserv.find('span',class_="num").text
        reserv=temp
        # --------------------------------------
        play=li.find('dl',class_ ="info_txt1").text
        playlist=play.split('|')   
        playtime=''
        for p in playlist:
            if p.count('분')==1:
                if p.count('개요') == 1:
                    p = p.replace('개요', '')
                playtime = p.strip()
                break
        str='%s,%s,%s,%s\n'%(title,rating,temp,playtime)
        f.write(str)
        