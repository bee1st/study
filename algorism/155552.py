import sys
x = list(map(int, sys.stdin.readline().split()))

for i in range(x[0]):
    y = list(map(int, sys.stdin.readline().split()))
    print(y[0] + y[1])