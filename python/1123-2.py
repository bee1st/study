# 이름과 태어난 년도를 입력받아 나이 태어난년도를 수정하세요
import pymysql as my

con = my.connect(host = 'localhost', user = 'root', password = '1234', db = 'pythondb', charset = 'utf8')
cur = con.cursor(my.cursors.DictCursor)
name = input('사용자 이름 = ')
birthyear = input('사용자 태어난 연도 = ')
sql = 'update member set age = %s, birthyear = %s where name = %s'
year = 2020 - int(birthyear) + 1
cur.execute(sql,(year, birthyear, name))
con.commit()
con.close()