# 변수 = open('파일명', 모드)
# 사용
# 변수.close() #자원반납
# 모드 : r(read), w(write), a(append)
# f = open('d:\\study\\pj1\\data\\poem.txt', 'r', encoding = 'utf-8')
# # txt = f.read() 전체 내용읽기
# txt = f.read(5) # 5글자 읽기
# print(txt)
# print(type(txt))
# f.close()
# print('*' * 30)
# f = open('data\\poem.txt', encoding ='utf-8') #리눅스는 '/'로 경로지정
# txt = f.readline() #한줄읽기
# print(txt)
# print(type(txt)) #문자열
# f.close()
#
# f = open('data\\poem.txt', encoding ='utf-8')
# txt = f.readlines() #줄단위 리스트 반환
# print(txt)
# print(type(txt)) #리스트
# f.close()
#
# print(type(txt))
# for line in txt:
#     print(line.strip())
# f.close()
#
# print('*' * 50)
# # with open('파일명', 모드) as 변수명:
# # with 블럭이 끝날때 자동 close
# with open('data\\poem.txt', encoding = 'utf-8') as f:
#     txt = f.read()
#     print(txt)
#
# print('-' * 50)
# with open('data\\test1.txt', 'w') as f:
#     f.write('very nice day')
#
# with open('data\\test2.txt', 'a', encoding='utf-8') as f:
#     for i in range(100):
#         f.write(str(i) + '\n')
#
# fruit = ['사과', '배', '포도']
# with open('data\\test2.txt', 'a', encoding = 'utf-8') as f:
#     # for a in fruit:  #같은 실행문
#     #     f.write(a)
#     f.writelines(fruit) #리스트를 파일에 쓰기
# with open('data\\test1.txt','w') as f:
#     print('test print',file=f)
# print('-'*30)
# col = ['이름', '나이', '주소']
# names = ['홍길동','심청','이몽룡','성춘향']
# age = [20, 16, 16, 16]
# juso = ['서울', '서산', '남원', '진주']
# with open('data\\addr.txt', 'w', encoding='utf-8') as f:
#     f.write(','.join(col)+'\n')
#     for i in range(len(names)):  #i=0,1,2,3
#         str='{},{},{}\n'.format(names[i], age[i], juso[i])
#         # print(str)
#         f.write(str)
# print('-'*30)
# a = ['one', 'two', 'three']
# # '연결문자'.join(리스트)
# print('-'.join(a))
# print('?'.join(a))
# print(type('?'.join(a)))
# b = ('one', 'two', 'three')
# print('-', join(b))
#이미지 저장

import requests #웹서버에 접근
url = 'http://bntnews.hankyung.com/bntdata/images/photo/201606/33ed99c856f314e91e0deeaeb99b6738.jpg'
rec = requests.get(url)
print(rec) #response[200] 성공
with open('img\\sana.jpg', 'wb') as f:  #b:binary
    f.write(rec.content)


