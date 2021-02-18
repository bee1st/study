import sys
N = list(map(int, sys.stdin.readline().split()))
def Factorial(n):
    if n == 1 or n == 0:
        return 1
    return n * Factorial(n - 1)

print(Factorial(N[0]))