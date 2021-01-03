# 파일 읽기, 쓰기
# 읽기 모드 : r, 
# 쓰기 모드(기존 파일 삭제) : w, 
# 추가 모드(파일 생성 또는 추가) : a

# 파일 읽기
# 예제 1
f = open('data\\dream.txt', 'r')
content = f.read()
print(content)
print(dir(f))
f.close() # 반드시 반환

# 예제 2
with open('data\\dream.txt', 'r', encoding='utf-8') as f:
    c = f.read()
    print(c)
    print(list(c))
    print(iter(c))

# 예제 3
with open('data\\dream.txt', 'r', encoding='utf-8') as f:
    for c in f:
        print(c.strip())

# 예제 4
with open('data\\dream.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    print(">", content)
    content = f.read() # 내용 없음
    print(">", content) 

# 예제 5
with open('data\\dream.txt', 'r', encoding='utf-8') as f:
    line = f.readline()
    # print(line)
    while line:
        print(line, end = '******')
        line = f.readline()

# 예제 6
with open('data\\dream.txt', 'r', encoding='utf-8') as f:
    contents = f.readlines() #리스트 리턴
    print(contents)
    for c in contents:
        print(c, end =' !! ')

# 예제 7
score = []
with open('data\\test2.txt', 'r', encoding='utf-8') as f:
    for line in f:
        score.append(int(line))
    print(score)

print('Avg : {:6.3}'.format(sum(score)/len(score)))

