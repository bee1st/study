import requests

# S_PAGENUMBER: 2
# S_MB_CD: W0726200
# S_HNAB_GBN: I
# hanmb_nm: G-DRAGON
# sort_field: SORT_PBCTN_DAY
import requests
from bs4 import BeautifulSoup
import cx_Oracle
con = cx_Oracle.connect("happy/day@localhost:1521/xe")
cursor = con.cursor()
sql = "insert into artist values (artist_seq.nextval, '{}', '{}', '{}')"
url='https://www.komca.or.kr/srch2/srch_01_popup_mem_right.jsp'
for i in range(1, 9):
    data = {'S_PAGENUMBER': i,
            'S_MB_CD': 10004134,
            'S_HNAB_GBN': 'I',
            'hanmb_nm': '이찬혁',
            'sort_field': 'SORT_PBCTN_DAY'
            }
    recvd = requests.post(url, data = data)
    dom=BeautifulSoup(recvd.text,'lxml')
    divs=dom.find_all('div',class_='board col')
    div=divs[1]
    tbody=div.find('tbody')
    trs=tbody.find_all('tr')
    for j in range(len(trs)):
        td=trs[j].find_all('td')
        title=td[0].text
        name=td[1].text
        zak=td[2].text
        # print(title, name, zak)
        cursor.execute(sql.format(title, name, zak))
con.commit()
con.close()
        
# 저작물명, 가수명, 작사를 오라클에 저장
