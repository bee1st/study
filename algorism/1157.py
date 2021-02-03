import sys
voca = sys.stdin.readline().upper()

box = list(set(voca[:-1]))
alphabat = []
for i in box:
    a = voca.count(i)
    alphabat.append(a)

if alphabat.count(max(alphabat)) > 1:
    print('?')
else :
    result = alphabat.index(max(alphabat))
    print(box[result])

