import sys
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))

print(a[0] * (b[0] % 10))
print(a[0] * ((b[0] // 10)%10))
print(a[0] * (b[0] // 100))
print(a[0] * b[0])