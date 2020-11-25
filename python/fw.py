#  파일 쓰기
# 예제 1
with open('data\\text1.txt', 'w', encoding='utf-8') as f:
    f.write("hello")

# 예제 2
with open('data\\text3.txt', 'w', encoding='utf-8') as f:
    f.write("python")

# 예제 3
from random import randint
with open('data\\text2.txt', 'w', encoding='utf-8') as f:
    for cnt in range(6):
        f.write(str(randint(1, 45)))
        f.write('\n')

# 예제 4
# writelines : 리스트 -> 파일로 저장
with open('data\\text2.txt', 'w', encoding='utf-8') as f:
    list = ['kim\n', 'yang\n', 'cho\n']
    f.writelines(list)

# 예제 5
with open('data\\text2.txt', 'w', encoding='utf-8') as f:
    print('이걸 테스트 중입니다.', file = f)
    print('이걸 테스트 중입니다.', file = f)

