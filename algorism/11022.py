import sys
a = list(map(int, sys.stdin.readline().split()))

for i in range(a[0]):
    x = list(map(int, sys.stdin.readline().split()))
    print("Case #{}: {} + {} = {}".format(i+1, x[0], x[1], x[0]+x[1]))