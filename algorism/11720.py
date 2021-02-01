import sys
x = list(map(int, sys.stdin.readline().split()))
y = sys.stdin.readline()

hap = 0
for i in range(x[0]):
    hap += int(y[i])

print(hap)
