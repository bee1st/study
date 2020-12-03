import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import time
import os
import cx_Oracle
# create table car(
#     no number constraint car_no_p primary key,
#     title varchar2(200),
#     price varchar2(200),
#     year varchar2(200),
#     baegi varchar2(200),
#     distance varchar2(200),
#     color varchar2(200),
#     trans varchar2(200),
#     guarantee varchar2(200),
#     fuel varchar2(200),
#     confirm varchar2(200)
# );
# create sequence car_seq;


def saveImg(imglist, title):
    # print(imglist)
    i = 0
    for imgurl in imglist:
        i = i + 1
        # filename = os.path.join('car', title.strip() +str(i) + imgurl[-4:])
        filename = os.path.join('d:\\','study','pj1','car', title.strip() +str(i) + imgurl[-4:])

        # print(filename)
        r1 = requests.get(imgurl)
        with open(filename, 'wb') as f:
            f.write(r1.content)

# https://www.bobaedream.co.kr/mycar/mycar_list.php?gubun=K&page=3&order=S11&view_size=20
# https://www.bobaedream.co.kr/mycar/mycar_list.php?gubun=K&page=1&order=S11&view_size=20
# https://www.bobaedream.co.kr/mycar/mycar_list.php?gubun=K&page=2&order=S11&view_size=20

con=cx_Oracle.connect('happy/day@localhost:1521/xe')
cur=con.cursor()
sql="insert into car values " \
    "(car_seq.nextval,'{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')"
url='https://www.bobaedream.co.kr/mycar/mycar_list.php?gubun=K&page={}&order=S11&view_size=20'
for page in range(1, 4):
    recvd=requests.get(url.format(page))
    dom = BeautifulSoup(recvd.text,'html.parser')
    alist = dom.select('#listCont div.mode-cell.title > p.tit > a')
    baseurl = 'https://www.bobaedream.co.kr/'
    urllist = []
    for a in alist:
        urllist.append(urljoin(baseurl,a['href']))
    for detailurl in urllist:
        r = requests.get(detailurl)
        detaildom = BeautifulSoup(r.text,'html.parser')
        title=detaildom.select_one('#bobaeConent div.title-area > h3').text
        price=detaildom.select_one('#bobaeConent div.price-area > span > b').text
        imgs=detaildom.select('#bx-pager img')
        imglist = []
        for img in imgs:
            if img['src'][2:6]=='file':
                imglist.append('https:'+img['src'])
        saveImg(imglist,title)
        infos = detaildom.select('#bobaeConent div.info-basic div > table tr')
        infolist = infos[0].text.strip().split('\n')
        year = infolist[1]
        baegi = infolist[3]
        infolist = infos[1].text.strip().split('\n')
        distance = infolist[1]
        color = infolist[3]
        infolist = infos[2].text.strip().split('\n')
        trans = infolist[1]
        guarantee = infolist[-1]
        infolist=infos[3].text.strip().split('\n')
        fuel = infolist[1]
        confirm = infolist[-1]
        if confirm == '확인사항':
            confirm =''
        cur.execute(sql.format(title,price,year,baegi,distance,color,trans,guarantee,fuel,confirm))
    time.sleep(1)
con.commit()
con.close()

# pyinstaller --onefile 파일명.py
# 명령프롬프트에서 실행시 윈도우+r - cmd
# C:\Users\admin>d:
# D:\>cd study\pj1\dist
# D:\study\pj1\dist>파일명