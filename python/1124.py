# create table music(
#     no number primary key,
#     title varchar2(100),
#     singer varchar2(100),
#     song varchar2(100)
#     );
# create sequence music_seq;


import requests
from bs4 import BeautifulSoup
# S_PAGENUMBER: 2
# S_MB_CD: W0726200
# S_HNAB_GBN: I
# hanmb_nm: G-DRAGON
# sort_field: SORT_PBCTN_DAY
import cx_Oracle
con = cx_Oracle.connect('happy/day@localhost:1521/xe')
cur = con.cursor()
sql = "insert into music values (music_seq.nextval, '{}', '{}', '{}') "
for page in range(1, 3):
    url='https://www.komca.or.kr/srch2/srch_01_popup_mem_right.jsp'
    data={'S_PAGENUMBER': page,
        'S_MB_CD': 'W0726200',
        'S_HNAB_GBN': 'I',
        'hanmb_nm': 'G-DRAGON',
        'sort_field': 'SORT_PBCTN_DAY'
        }
    recvd=requests.post(url,data=data)
    # print(recvd)
    # 1페이지에 있는 저작물명,가수명,작사를 오라클에 저장하세요
    dom = BeautifulSoup(recvd.text, 'lxml')
    tables = dom.find_all('table')
    # print(len(tables)) #2
    trs = tables[1].find_all('tr')
    # print(len(trs)) #11
    for i in range(1, len(trs)):
        tds = trs[i].find_all('td')
        title = tds[0].text
        singer = tds[1].text
        song = tds[2].text
        # print(title, singer, song)
        cur.execute(sql.format(title, singer, song))
con.commit()
con.close()





