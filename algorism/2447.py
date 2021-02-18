import sys
N = list(map(int, sys.stdin.readline().split()))

def star(N):
    return '*' * star(N)

print(star(N[0]))