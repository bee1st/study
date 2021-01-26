import sys
x = list(map(int, sys.stdin.readline().split()))
yoon = x[0]

if (yoon % 4 == 0):
    if (yoon % 100 != 0):
        print(1)
    elif (yoon % 400 == 0):
        print(1)
    else :
        print(0)
else :
    print(0)