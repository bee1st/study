import sys
x = list(map(int, sys.stdin.readline().split()))
int a
for i in range(1, x[0] + 1):
    for j in range(x[0], 0, -1):
        a[i] = j * "*"
        print(a[i])

    