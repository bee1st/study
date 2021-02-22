import sys
N = int(sys.stdin.readline())
box = []
for i in range(N):
    n = int(sys.stdin.readline())
    box.append(n)
box.sort()
print(round(sum(box) / N))
print(box[N//2])
# if N == 1:
#     print(box[0])
# else :
#     print(box[1]  #최빈값 구하기만 하면됨
if N == 1:
    print(0)
else:
    print(box[N - 1] - box[0])