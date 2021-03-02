# 2차원 공간(행렬)
for i in range(5):
    for j in range(5):
        print('(', i, ',', j, ')', end=' ')
    print()

# 동, 북, 서, 남
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
# 현재 위치
x, y = 2, 2
for i in range(4):
    # 다음위치
    nx = x + dx[i] #행
    ny = y + dy[i] #열
    print(nx, ny)

# 입력받기
n = int(input())
x, y = 1, 1
plans = input().split()

# L, R, U, D 에 따른 이동 방향
dx = [0, 0, -1, 1] 
dy = [-1, 1, 0, 0] 
move_types = ['L', 'R', 'U', 'D']

# 이동 계획을 하나씩 확인하기
for plan in plans:
    # 이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    # 공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    # 이동수행
    x, y = nx, ny
print(x, y)