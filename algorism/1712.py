# 풀이
# 고정비용 A
# 가변비용 B 
# 노트북 가격 C
# 손익분기점 = 총 수입(판매비용) > 고정비용 + 가변비용

import sys
x = list(map(int, sys.stdin.readline().split()))
A = x[0]
B = x[1]
C = x[2]

# A + B * (a) > C * (a)
if B >= C :
    print(-1)
else :
    print(A // (C - B) + 1)







