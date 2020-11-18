import requests
from bs4 import BeautifulSoup
url='https://finance.naver.com/marketindex/'
recvd=requests.get(url)
# print(recvd)
# print(recvd.text)
dom=BeautifulSoup(recvd.text,'lxml')
span = dom.find('span', class_ = 'value')
print(span)

