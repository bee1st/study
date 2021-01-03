# mariadb - 10.3.27 - winx64.msi

# show databases; 데이터베이스 목록확인
# use pythondb; 데이터베이스 선택
# use tables; 테이블목록확인

import pymysql as my

# 1) 데이터베이스 연결
con = my.connect(host = 'localhost', user = 'root', password = '1234', db = 'pythondb', charset = 'utf8')

# 2) 커서생성
# cur = con.cursor()
cur = con.cursor(my.cursors.DictCursor)

# 3) 쿼리생성
# sql = 'select * from member'
while(True):
    name = input('사용자 이름 = ')
    if name == "":
        break
    age = input('사용자 나이 = ')
    email = input('사용자 이메일 = ')
    birthyear = input('사용자 태어난 연도 = ')
    sql = 'insert into member (name, age, email, birthyear) values (%s, %s, %s, %s)'
# 4) 실행처리
    cur.execute(sql, (name, age, email, birthyear))
con.commit()
# cur.execute(sql)
# rows = cur.fetchall()
# for row in rows:
#     print(row)
#     print(row['no'], row['name'], row['age'], row['email'], row['birthyear'])

# 5) 자원해제
con.close()
