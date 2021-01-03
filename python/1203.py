import cx_Oracle
import os
import sys
import urllib.request
import json
client_id = "Z7yRwPXHYKA9P4sJINTn"
client_secret = "AgOcWdg0NL"
encText = urllib.parse.quote("머신러닝")
con = cx_Oracle.connect('happy/day@localhost:1521/xe')
cur = con.cursor()
sql="insert into book values (book_seq.nextval,'{}','{}','{}','{}','{}','{}')"
# url = "https://openapi.naver.com/v1/search/book.json?start=1&display=100&query=" + encText # json 결과
# url = "https://openapi.naver.com/v1/search/book.json?start=101&display=100&query=" + encText # json 결과
url = "https://openapi.naver.com/v1/search/book.json?start={}&display=100&query=" + encText # json 결과
for s in range(1, 200, 100):
    request = urllib.request.Request(url.format(s))
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        result = response_body.decode('utf-8')
    else:
        print("Error Code:" + rescode)
    dic = json.loads(result)
    # print(dic)
    for d in dic['items']:
        title = d['title'].replace('<b>머신러닝</b>', '머신러닝')
        title = title.replace("'", "")
        img = d['image']
        if img.find('?') != -1:
            img = img[:img.index('?')]
        author = d['author']
        price = d['price']
        publisher = d['publisher']
        description=d['description'].replace('<b>머신러닝</b>','머신러닝').replace('<b>머신 러닝</b>','머신러닝')
        description = description.replace("'","")
        description = description.replace('■ ','').replace('★','')
        cur.execute(sql.format(title,img,price,publisher,author,description))
        print('제목:'+title)
        print('이미지경로:'+img)
        print('가격:'+price)
        print('출판사:'+publisher)
        print('저자:'+author)
        print('상세내용:'+description)


con.commit()
con.close()

    # create table book(
    #     no number primary key,
    #     title varchar2(300),
    #     img varchar2(300),
    #     price varchar2(300),
    #     publisher varchar2(300),
    #     author varchar2(300),
    #     description varchar2(2000)
    # );
    # create sequence book_seq;