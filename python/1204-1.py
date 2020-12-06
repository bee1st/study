import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
url="https://www.alexa.com/topsites"
recvd=requests.get(url)
# print(recvd)
dom = BeautifulSoup(recvd.text,'lxml')
trs = dom.select('#alx-content div.listings.table > div')
i = 0
for tr in trs:
    i = i + 1
    if i == 1:
        continue
    print(tr)
    divs = tr.find_all('div')
    # print(len(divs))
    rank = divs[0].text
    name = divs[1].text
    print(rank, name)
    # for div in divs:
    #     print(div.text)
    break