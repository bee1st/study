import sys
x = list(map(int, sys.stdin.readline().split()))

for i in range(1, x[0] + 1):
    print(i * "*")

