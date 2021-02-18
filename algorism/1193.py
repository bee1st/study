#  1/1 -> 1/2 -> 2/1 -> 3/1 -> 2/2 -> ...
# 순서대로 1,2,3,4,5번 ...
# x가 주어졌을때 x번째 분수를 구하시오

#         1/1  1
#       1/2 2/1  2
#      3/1 2/2 1/3  3
#    1/4 2/3 3/2 4/1  4
# 5/1 3/2 3/3 2/4 1/5  5

X = int(input())
target = 0
for i in range(1, 1000000):
    if target + i >= X:
        # 이 라인에 있구나!
        if i % 2 == 0:
            # 짝수야!
            print(X - target, "/", i - (X - target) + 1, sep="")
        else:
            # 홀수야!
            print(i - (X - target) + 1, "/", X - target, sep="")
        break
    target += i





