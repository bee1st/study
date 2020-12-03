import requests
from bs4 import BeautifulSoup
def saveImg(imgUrl, title):
    # print(imgUrl)
    # print(imgUrl.index('?'))
    # print(imgUrl[imgUrl.index('?')-4:imgUrl.index('?')]) #imgUrl[92:96]
    print(title)
    title = title.replace('[', '')
    title = title.replace(']', '')
    title = title.replace("'", "")
    title = title.replace('?', '')
    title = title.replace(",", "")
    filename = 'img\\' + title + imgUrl[imgUrl.index('?')-4:imgUrl.index('?')]
    print(filename)
    r = requests.get(imgUrl)
    f = open(filename, 'wb')
    f.write(r.content)
    f.close()

def makeData(pageUrl):
    r=requests.get(pageUrl)
    # print(r)
    d=BeautifulSoup(r.text,'lxml')
    imgUrl=d.find('div',id="newsEndContents").find('img')['src']
    title=d.find('h4').text
    saveImg(imgUrl, title)
    # print(imgUrl)
    # print(title)
    content=d.find('div',id="newsEndContents").text
    # print(content)
    str='{}::\n{}'.format(title,content)
    print(str)
url='https://sports.news.naver.com/index.nhn'
recvd=requests.get(url)
# print(recvd)
# print(recvd.text)
dom=BeautifulSoup(recvd.text,'lxml')
aes=dom.find_all('a',class_="link_today")
# print(len(aes))
for a in aes:
    # print(a['href'])
    pageUrl='https://sports.news.naver.com'+a['href']
    # print(pageUrl)
    makeData(pageUrl)
    break