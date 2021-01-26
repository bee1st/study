import sys
x = list(map(int, sys.stdin.readline().split()))

h = x[0]
m = x[1]

m = h * 60 + m

# 총 몇분인지만 관심을 갖는다!
m = m - 45

if m < 0:
    m = m + (24 * 60)

print(m // 60, m % 60)


# 시간 변환 이런문제
# 무조건 가장작은 단위로 바꿔


# if h == 0:
#     if m == 45:
#         print(0, 0)
#     else :
#         time = (24 * 60) + m - 45
#         print((time // 60), (time % 60)) 
# else :
#     time = ((h * 60) + m) - 45 
#     print((time // 60), (time % 60)) 



# if h > 0:
#     if m >= 45:
#         print(h, m - 45)
#     elif m < 45:
#         print(h - 1, 60 + m - 45)
# else:
#     if m < 45:
#         print(23, 60 + m - 45)
#     else :
#         print(h, m - 45)


