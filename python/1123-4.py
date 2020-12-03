# create table webtoon(
#     no number primary key,
#     title varchar2(100),
#     rating varchar2(20),
#     regdate varchar2(20)
# );
# create sequence webtoon_seq;
# insert into webtoon values (webtoon_seq.nextval, 제목, 평점, 등록일);


# import requests
# from bs4 import BeautifulSoup
# import cx_Oracle
# con = cx_Oracle.connect("happy/day@localhost:1521/xe")
# cursor = con.cursor()
# sql = 'insert into webtoon values (webtoon_seq.nextval, :1, :2, :3)'
# sql = "insert into webtoon values (webtoon_seq.nextval, '{}', '{}', '{}')"
# url='https://comic.naver.com/webtoon/list.nhn?titleId=733766&weekday=mon'
# recvd=requests.get(url)
# dom=BeautifulSoup(recvd.text,'lxml')
# table=dom.find('table',class_="viewList")
# trs=table.find_all('tr')
# for i in range(2,len(trs)):
#     td=trs[i].find('td')
#     img=td.find('img')['src']  
#     td1=trs[i].find('td',class_='title')
#     title=td1.find('a').text
#     div=trs[i].find('div',class_="rating_type")
#     rating=div.find('strong').text
#     regdate=trs[i].find('td',class_="num").text
#     cursor.execute(sql, (title, rating, regdate))
# con.commit()
# con.close()

#-------------------------------------------------
import requests
from bs4 import BeautifulSoup
import cx_Oracle
con = cx_Oracle.connect("happy/day@localhost:1521/xe")
cursor = con.cursor()
sql = "insert into webtoon values (webtoon_seq.nextval, '{}', '{}', '{}')"
url='https://comic.naver.com/webtoon/list.nhn?titleId=733766&weekday=mon'
recvd=requests.get(url)
dom=BeautifulSoup(recvd.text,'lxml')
table=dom.find('table',class_="viewList")
trs=table.find_all('tr')
for i in range(2,len(trs)):
    td=trs[i].find('td')
    img=td.find('img')['src']  
    td1=trs[i].find('td',class_='title')
    title=td1.find('a').text
    div=trs[i].find('div',class_="rating_type")
    rating=div.find('strong').text
    regdate=trs[i].find('td',class_="num").text
    cursor.execute(sql.format(title, rating, regdate))
con.commit()
con.close()
