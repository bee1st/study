T = int(input())
for i in range(T):
    k = int(input())
    n = int(input())
    room = [r for r in range(1, n + 1)] #아파트 호수
    # print('room=', room)
    # print(room)
    for a in range(k): #층수만큼 반복
        # print('a = ', a)
        for b in range(1, n): #1호는 1이므로 2호부터 n호까지 ..
            # print('b = ', b)
            room[b] += room[b - 1] # 해당 호수에 이전 호값을 더한다. (누적)
            # print(room)
        # print(room)
    print(room[-1])



# 0층 i호 -> i명
# j층 1호 -> 1명
# 1층 3호 -> 1층 2호 사람수 + 0층 3호 사람수
# 2층 3호 -> 2층 2호 사람수 + 1층 3호 사람수

# k층 n호 -> k층 n-1호 + k-1층 n호
# room[k][n] -> room[k][n-1] + room[k-1][n]
