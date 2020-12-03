import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import time
url='https://www.bobaedream.co.kr/mycar/mycar_list.php?gubun=K'
recvd=requests.get(url)
# print(recvd)
# 상세페이지의 차이름,가격,기본정보를 데이터베이스에 입력, 이미지 car폴더에 저장
dom = BeautifulSoup(recvd.text,'lxml')
alist = dom.select('#listCont div.mode-cell.title > p.tit > a')
# print(len(alist))
baseurl = 'https://www.bobaedream.co.kr/'
urllist = []
for a in alist:
    # print(baseurl+a['href'])
    # print(urljoin(baseurl,a['href']))
    urllist.append(urljoin(baseurl,a['href']))
# print(urllist)
for detailurl in urllist:
    r = requests.get(detailurl)
    # print(r)
    detaildom = BeautifulSoup(r.text,'lxml')
    title=detaildom.select_one('#bobaeConent div.title-area > h3').text
    # print(title)
    price=detaildom.select_one('#bobaeConent div.price-area > span > b').text
    # print(price)
    imgs=detaildom.select('#bx-pager img')
    # print(imgs)
    imglist = []
    for img in imgs:
        # print('https:'+img['src'])
        if img['src'][2:6]=='file':
            imglist.append('https:'+img['src'])
    # print(imglist)
    infos = detaildom.select('#bobaeConent div.info-basic div > table tr')
    # print(len(infos))
    # print(infos[0].text)
    infolist = infos[0].text.strip().split('\n')
    # print(infolist)
    year = infolist[1]
    baegi = infolist[3]

    infolist = infos[1].text.strip().split('\n')
    distance = infolist[1]
    color = infolist[3]

    infolist = infos[2].text.strip().split('\n')
    # print(infolist)
    trans = infolist[1]
    guarantee = infolist[-1]

    infolist=infos[3].text.strip().split('\n')
    fuel = infolist[1]
    confirm = infolist[-1]
    if confirm == '확인사항':
        confirm ==''

    str = "{}, {}, {}, {}, {}, {}, {}, {}, {}, {}"
    print(str.format(title,price,year,baegi,distance,color,trans,guarantee,fuel,confirm))
print('-' * 50)
