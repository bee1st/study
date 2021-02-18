# 정확하게 N킬로그램을 배달
# 봉지는 3, 5킬로그램
# 최대한 적은 봉지 ex) 18kg -> 3 * 6 말고 5 * 3 + 3 * 1 
# 정확하게 N킬로그램을 만들수 없다면 -1 출력

# N = 5 * a + 3 * b
N = int(input())
bong = 0
for i in range(N):
    for j in range(N):
        bong = (3 * i) + (5 * j)
        if bong == N:
            print(i + j) #4, 6두개 나오는데 맨처음것만 출력하게 할 방법...
            exit()
if N == 4 or N == 7:
    print(-1)


# N = int(input())

# c = [0 for i in range(N + 1)]

# for i in range(1, (N // 5) + 1):
#     c[i * 5] += i


# for i in range(1, (N // 3) + 1):
#     if c[i * 3] == 0:
#         c[i * 3] = min(i, c[(i * 3) - 3] + 1)
#     else:
#         c[i * 3] = min(c[i * 3], c[(i * 3) - 3] + 1)

# if c[N] == 0:
#     print(-1)
# else:
#     print(c[N])


