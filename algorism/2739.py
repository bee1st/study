import sys
x = list(map(int, sys.stdin.readline().split()))

a = x[0]

for i in range(1, 9 + 1):
    print(a,"*",i,"=",a * i)