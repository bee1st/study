import sys
x = list(map(int, sys.stdin.readline().split()))
jumsu = list(map(int, sys.stdin.readline().split()))

M = max(jumsu)
avg = 0
for i in range(x[0]):
    avg += jumsu[i] / M * 100

print(avg / x[0])