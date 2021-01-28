import sys

while(True):
    try:
        x = list(map(int, sys.stdin.readline().split()))
        print(x[0] + x[1])
    except:
        break
