import sys
a = int(input())
for i in range(a):
    x = list(map(int, sys.stdin.readline().split()))
    avg = sum(x[1:]) / x[0]
    count = 0
    for j in x[1:]:
        if j > avg:
            count += 1
    print(("%.3f" %round((count/x[0]) * 100, 3)),"%", sep='')

