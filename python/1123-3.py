import pymysql as my
import requests
from bs4 import BeautifulSoup
con = my.connect(host = 'localhost', user = 'root', password = '1234', db = 'pythondb', charset = 'utf8')
cur = con.cursor(my.cursors.DictCursor)
sql = 'insert into movies (title, rating, reserv, playtime) values (%s, %s, %s, %s)'
url='https://movie.naver.com/movie/running/current.nhn'
recvd = requests.get(url) 
dom = BeautifulSoup(recvd.text, 'lxml')
ul = dom.find('ul', class_ = "lst_detail_t1") 
lis = ul.find_all('li')
for li in lis:
    img=li.find('img')['src']
    title=li.find('dt',class_ ="tit").find('a').text
    rating=li.find('span',class_="num").text
    reserv=li.find('div', class_="star_t1 b_star")
    if reserv==None :
        temp = ''
    else:
        temp=reserv.find('span',class_="num").text
    reserv=temp
    play=li.find('dl',class_ ="info_txt1").text
    playlist=play.split('|')   
    playtime=''
    for p in playlist:
        if p.count('분')==1:
            if p.count('개요') == 1:
                p = p.replace('개요', '')
            playtime = p.strip()
            break
    cur.execute(sql, (title, rating, temp, playtime))
con.commit()
con.close()
