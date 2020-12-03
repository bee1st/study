import pymysql as my

con = my.connect(host = 'localhost', user = 'root', password = '1234', db = 'pythondb', charset = 'utf8')
cur = con.cursor(my.cursors.DictCursor)
age = input('사용자 나이 = ')
sql = 'delete from member where age = %s'
cur.execute(sql, (age,)) #튜플이라 ,를 해주는게 좋다
con.commit()
con.close()