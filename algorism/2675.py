import sys
T = int(input())
b = []
for i in range(T):
    S = sys.stdin.readline()
    a = []
    for j in range(1, len(S)):
        a += int(S[0]) * S[j]
    b = (''.join(a).split())
    print(b[0])

