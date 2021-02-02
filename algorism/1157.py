import sys
voca = sys.stdin.readline().upper()
box = list(set(voca))
alphabat = []
for i in box:
    a = voca.count(i)
    alphabat.append(a)

if alphabat.count(max(alphabat)) > 1:
    print('?')
else :
    max_cnt = alphabat.index(max(alphabat))
    print(box[max_cnt])