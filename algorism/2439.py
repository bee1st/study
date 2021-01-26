import sys
x = list(map(int, sys.stdin.readline().split()))

for i in range(x[0]):
    i += 1
    print(" " * (x[0] - i) + "*" * i)