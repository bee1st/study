import sys
x = sys.stdin.readline()
box = 'abcdefghijklmnopqrstuvwxyz'
a = []
for i in box:
    a = x.find(i)
    print(a, end=' ')
