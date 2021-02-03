import sys
x = sys.stdin.readline().upper()
dial = ['ABC','DEF','GHI','JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
time = 0

for i in range(len(dial)):
    for j in x:
        print(i, dial[i], j, dial[i] in j)
        if j in dial[i]:
            time += dial.index(dial[i]) + 3

print(time)
        

