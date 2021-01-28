import sys
N = list(map(int, sys.stdin.readline().split()))[0]
n = N

cycle_count = 0
while(True):
    cycle_count = cycle_count + 1
    if N < 10:
        a = N
    else:
        a = N % 10
        N = (N // 10) + (N % 10)
    b = N % 10
    N = (a * 10) + b
    if N == n:
        break

print(cycle_count)





