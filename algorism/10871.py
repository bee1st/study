import sys
x = list(map(int, sys.stdin.readline().split()))
y = list(map(int, sys.stdin.readline().split()))
N = x[0]
X = x[1]

for i in range(N):
    if y[i] < X:
        a = y[i]
        print(a, end=' ')

