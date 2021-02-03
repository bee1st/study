import sys
x = sys.stdin.readline()
box = 'abcdefghijklmnopqrstuvwxyz'
a = []
for i in box:
    print(i)
    a = x.find(i)
    print(a)

    