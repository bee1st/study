import sys
x = sys.stdin.readline().upper()
dial = ['ABC','DEF','GHI','JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
time = 0
for s in x:
    for i in range(len(dial)):
        if s in dial[i]:
            time += (i + 3)
print(time)
