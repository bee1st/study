import cx_Oracle
import os
import sys
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
con = cx_Oracle.connect('big/small@localhost:1521/xe')
cur = con.cursor()
sql="insert into ranking values (ranking_seq.nextval,'{}','{}','{}','{}','{}','{}')"
url="https://www.alexa.com/topsites"
recvd=requests.get(url)
# print(recvd)
dom = BeautifulSoup(recvd.text,'lxml')
alist = dom.select('#alx-content div.listings.table > div')
i = 0
for sitelist in alist:
    i = i + 1
    if i == 1:
        continue
    divs = sitelist.find_all('div')
    rank = divs[0].text
    site = divs[1].text
    dts = divs[2].text
    dpv = divs[3].text
    tfs = divs[4].text
    tsl = divs[5].text
    cur.execute(sql.format(rank,site,dts,dpv,tfs,tsl))
    print('rank : ' + rank)
    print('site : ' + site)
    print('Daily Time on Site : ' + dts)
    print('Daily Pageviews per Visitor : ' + dpv)
    print('"%"' + 'of Traffic From Search : ' + tfs)
    print('Total Sites Linking In : ' + tsl)
    print('*' * 40)

con.commit()
con.close()

    # create table ranking(
    #     no number primary key,
    #     rank varchar2(3000),
    #     site varchar2(3000),
    #     dts varchar2(3000),
    #     dpv varchar2(3000),
    #     tfs varchar2(3000),
    #     tsl varchar2(3000)
    # );
    # create sequence ranking_seq;
