import sys
n = list(map(int, sys.stdin.readline().split()))

def fibo(n):
    if n <= 1:
        return n
    return fibo(n - 1) + fibo(n - 2)

print(fibo(n[0]))