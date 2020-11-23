# import bs4
# import requests
# url = 'https://www.naver.com'
# recv = requests.get(url)
# print(recv)   #접근결과코드
# print(recv.text) # html코드
# print(recv.encoding)
# print(recv.headers)



from bs4 import BeautifulSoup
#웹페이지에 접근하여 태그 인식
f = open('data\\poem.txt', encoding = 'utf-8').read()
# print(f)
# BeautifulSoup(웹페이지, 파싱방식)
# 파싱 : html.parser, html5lib,lxml
# dom = BeautifulSoup(f, 'html.parser')
dom = BeautifulSoup(f, 'lxml')
# print(dom)
# dom.find('태그')   첫번째 태그 추출
# dom.태그
# div=dom.find('div')
# div=dom.div
# print(div)
# dom.find_all('태그')  모든 태그추출,리스트반환
# divs=dom.find_all('div')
# print(divs)  #[div,div,....]
# -------------------------------
# firstdiv=dom.div
# div2=firstdiv.div
# print(div2)
# ps=div2.find_all('p')
# print(ps)
# print('*'*30)
# dom.find('태그',class_='클래스명')
# dom.find('태그',{'class':'클래스명'})
# cl=dom.find('div',class_='ex_class')
# cl=dom.find(class_='ex_class')
# print(cl)
cl=dom.find('div',{'class':'ex_class'})
print(cl)

# dom.find_all('태그',class_='클래스명')
# dom.find_all(class_='클래스명')
# dom.find_all('태그',{'class':'클래스명'})

# exs=dom.find_all('div',class_='ex_class')

# exs=dom.find_all(class_='ex_class')
# exs=dom.find_all('div',{'class':'ex_class'})
# exs=dom.find_all('div',{'class':'ex_class'})
# print(exs)
sisters = dom.find_all({'class' : 'sister'})
print(sisters)
#id가 third인 모든태그
thirds = dom.find_all(id = 'third')
print(thirds)
#id가 third인 모든 태그의 첫번째 p태그
print(thirds[0])
print('~' * 50)
p1 = thirds[0].find('p')
print(p1)
# a = ['one']
# print(a[0])
# b = 'one'
# print(b)