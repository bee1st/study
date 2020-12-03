import cx_Oracle
class DBManager:
    def __init__(self):
        self.con = cx_Oracle.connect('happy/day@localhost:1521/xe')
        self.cur = self.con.cursor()
        print('연결성공')
    def __del__(self):
        print('연결해제')
        self.con.close()
    def selectAll(self):
        sql = "select * from webtoon order by no"
        self.cur.execute(sql)
        rows = self.cur.fetchall()
        for row in rows:
            print(row[0], row[1], row[2], row[3])
    def selectRating(self, rating):
        sql = "select * from webtoon where rating >= {}"
        self.cur.execute(sql.format(rating))
        rows = self.cur.fetchall()
        for row in rows:
            print(row[0], row[1], row[2], row[3])
    def insert(self, title, rating, regdate):
        sql = "insert into webtoon values (webtoon_seq.nextval, '{}','{}','{}')"
        self.cur.execute(sql.format(title, rating, regdate))
        self.con.commit()
    def updateRegdate(self, rating, regdate):
        sql = "update webtoon set regdate ='{}' where rating >= {}" 
        self.cur.execute(sql.format(regdate, rating))
        self.con.commit()
    def deleteRating(self, rating):
        sql = "delete from webtoon where rating >= {}"
        self.cur.execute(sql.format(rating))
        self.con.commit()
        pass

d1 = DBManager()
# d1.insert('둘리', '4.999', '1999.01.02')
# d1.selectAll()
# d1.selectRating(9.95)
# d1.updateRegdate(8.1, "2020-12-24")
# d1.selectAll()
# d1.deleteRating(9.9)
# d1.selectAll

color = ['red', 'green', 'blue']
fruit = ['apple', 'orange', 'cherry', 'tomato']
number = ['one','two', 'three']
for t in zip(color, fruit):
    print(t)
for t in zip(color, fruit, number):
    print(t)
for c, f, n in zip(color, fruit, number):
    print(c, f, n)