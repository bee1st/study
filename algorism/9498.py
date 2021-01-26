import sys
x = list(map(int, sys.stdin.readline().split()))

a = x[0]
if a >= 90 and a <= 100:
    print("A")
elif a >= 80:
    print("B")
elif a >= 70:
    print("C")
elif a >= 60:
    print("D")
else :
    print("F")