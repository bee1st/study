import sys
a = list(map(int, sys.stdin.readline().split()))
A = a[0]
B = a[1]
C = a[2]

print((A+B)%C)
print(((A%C) + (B%C))%C)
print((A*B)%C)
print(((A%C) * (B%C))%C)
