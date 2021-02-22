import sys
N = list(map(int, sys.stdin.readline().split()))
M = N[1]
box = 0
black = []

c = list(map(int, sys.stdin.readline().split()))
for j in range(N[0]):
    for k in range(N[0]):
        for h in range(N[0]):
            if (j != k and k != h and j != h):
                box = c[j] + c[k] + c[h]
                if box <= M:
                    black.append(box)
            
black.sort()
print(black[-1])


