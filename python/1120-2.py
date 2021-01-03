import sqlite3
# 1) 데이터베이스 연결
con = sqlite3.connect('d:\\sqlite\\pythondb')

# 2) 커서 생성
cur = con.cursor()

while(True):
    id = input('사용자 아이디 = ')
    if id == "":
        break
    name = input('사용자 이름 = ')
    age = input('사용자 나이 = ')
    email = input('사용자 이메일 = ')
    birthyear = input('사용자 태어날연도 = ')

    # 3) 쿼리생성
    # sql = "insert into member values('" + id + "','" + name + "'," + age + ",'" + email + "'," + birthyear + ")"
    sql = "insert into member values ('{}', '{}', '{}', '{}', '{}') ".format(id, name, age, email, birthyear)
    print(sql)
    # sql = "delect from member"
    # 4) 실행처리
    cur.execute(sql)
con.commit()
    # while (True):
    #     row = cur.fetchone()
    #     if row == None:
    #         break
    #     # print(row)
    #     print(row[0], row[1], row[2], row[3], row[4])

# 5) 자원해제
con.close()