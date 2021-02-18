import sys
a = int(input())
for i in range(a):
    x = list(map(int, sys.stdin.readline().split()))
    H = x[0]
    W = x[1]
    N = x[2]
    floor = N % H
    ho = (N // H) + 1
    if floor == 0:
        floor = H
        ho = (N // H)
    print((100 * floor) + (ho))