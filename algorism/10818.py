import sys
x = list(map(int, sys.stdin.readline().split()))
N = list(map(int, sys.stdin.readline().split()))


min = 1000001
max = -1000001
for i in range(x[0]):
    if max < N[i]:
        max = N[i]
    if min > N[i]:
        min = N[i]
print(min, max)

# N.sort()
# min = N[0]
# max = N[x[0] - 1]
# print(min, max)
# 속도가 느림
