from bs4 import BeautifulSoup
with open('data\\test.html', mode='r', encoding = 'utf-8') as f :
    txt = f.read()
# print(txt)
# print(type(txt))
dom = BeautifulSoup(txt, 'lxml')
# div = dom.find('div') #div인 첫번째 태그
# print(div)

# divs = dom.find_all('div') #div인 모든 태그
# print(divs)

# div 태그중에 클래스가 'ex_class'인것 첫번째 추출
# divs = dom.find('div', {'class' : 'ex_class'})
# print(divs)

# div 태그중에 클래스가 'ex_class'인것 모두 추출
# divs = dom.find_all('div', {'class': 'ex_class'})
# print(divs)

# 클래스가 'ex_class'인것 모두 추출
# divs = dom.find_all(class_ = 'ex_class')
# print(divs)

# id가 'ex_class'인것 모두 추출
ids = dom.find(id = 'ex_id')
# print(ids)

#id 'ex_id' 인것중 모든 p태그
ps = ids.find_all('p')
# print(ps)

#data 추출
# dom.string
# dom.txt
# dom.get_text()

#속성 추출
# dom['속성']
# dom.get('속성')
# dom.attrs['속성']

title = dom.find('title')
# print(title)
# print(title.string)
# print(title.text)
# print(title.get_text())

# a의 내용 추출
aes = dom.find_all('a')
# print(aes)
# for a in aes:
#     print(a.text)
#     print(a['href'])

# id가 link2인 요소의 class 추출
# a = dom.find(id = 'link2').get('class')
# print(a)
# print(dom.find(id = 'link2').get('class'))

#dom 추적
#dom.parent 부모
#dom.parents 조상, 객체로 반환
#dom.children 자식
#dom.descendants 자손
# dom.next_siblings 아래쪽 형제요소
# dom.previous_siblings 위쪽 형제요소


# title = dom.find('p', class_ = 'title')
# print(title)
# print('*' * 50)
# print('parent', title.parent)
# print('*' * 50)
# print('parents', title.parents)
# for p in title.parents:
#     print(p)
#     print('-_-_' * 20)

#id가 second인 div
div = dom.find(id = 'second')
# print(div)
# divchild = div.children
# print('-' * 50)
# print(divchild)
# for c in divchild:
#     print(c)
#     print('!'*30)

# divdes = div.descendants
# print(divdes)
# print('*' * 50)
# for d in divdes:
#     print(d)
#     print('-' * 70)

#id가 link2인 a의 형제찾기
a = dom.find(id = 'link2')
print(a)
anext= a.next_siblings
print(anext)
for temp in anext:
    print(temp)
    print('$' * 30)