import sys
x = list(map(int, sys.stdin.readline().split()))
y = list(map(int, sys.stdin.readline().split()))

a = x[0]
b = y[0]

if (a > 0 and b > 0):
    print(1)
elif (a < 0 and b > 0):
    print(2)
elif (a < 0 and b < 0):
    print(3)
else :
    print(4)