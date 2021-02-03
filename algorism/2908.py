import sys
score = sys.stdin.readline().split()

a = score[0]
b = score[1]

a1 = int(a[::-1])
b1 = int(b[::-1])

if a1 > b1 :
    print(a1)
else :
    print(b1)


