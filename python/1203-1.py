import pymysql as my
# 1)데이터베이스 연결
con=my.connect(host='localhost',user='root',password='1234',
               db='pythondb', charset='utf8')
# 2)커서생성
# cur=con.cursor()
cur=con.cursor(my.cursors.DictCursor)
# 3)쿼리생성
sql='select * from member'
# 4)실행 처리
cur.execute(sql)
rows=cur.fetchall()
print(rows)   #[{},{},{}]
for row in rows:
    # print(row)
    print(row['no'],row['name'],row['age'],row['email'],row['birthyear'])
# # 5)자원해제
con.close()
#------------
# # 1)데이터베이스 연결
# con=my.connect(host='localhost',user='root',password='1234',
#                db='pythondb', charset='utf8')
# # 2)커서생성
# cur=con.cursor(my.cursors.DictCursor)
# # 3)쿼리생성
# while(True):
#     name=input('사용자이름=')
#     if name=="":
#         break
#     age=input('사용자나이=')
#     email=input('사용자이메일=')
#     birthyear=input('사용자태어난년도=')
#     sql='insert into member (name,age,email,birthyear) values (%s,%s,%s,%s)'
#     # 4)실행 처리
#     cur.execute(sql,(name,age,email,birthyear))
# con.commit()
# # # 5)자원해제
# con.close()
# ------------------
# con=my.connect(host='localhost',user='root',password='1234',db='pythondb', charset='utf8')
# cur=con.cursor(my.cursors.DictCursor)
# age=input('나이=')
# sql='delete from member where age<=%s'
# cur.execute(sql,(age,))
# con.commit()
# con.close()
# 이름과 태어난 년도를 입력받아 나이,태어난년도를 수정하세요
# con=my.connect(host='localhost',user='root',password='1234',db='pythondb', charset='utf8')
# cur=con.cursor(my.cursors.DictCursor)
# name=input('이름=')
# birthyear=input('태어난년도=')
# sql='update member set age=%s, birthyear=%s where name=%s'
# nai=2020-int(birthyear)+1
# cur.execute(sql,(nai,birthyear,name))
# con.commit()
# con.close()