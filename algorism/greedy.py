# 그리디 알고리즘
# 지금 현재 상황에서 지금 당장 좋은 것만 고르는 방법

# n = int(input())
# arr = [500, 100, 50, 10]
# count = 0
# for i in arr:
#     count += n // i
#     n %= i
# print(count)
# -------------------------------------------------------------

# n, k = map(int, input().split())
# count = 0

# while True:
#     target = (n // k) * k # N이 K로 나누어 떨어지는 수가 될 때까지 빼기
#     count += (n - target)
#     n = target 
#     if n < k :
#         break # N이 K보다 작을때 반복문 탈출
#     count += 1
#     n //= k
# count += (n - 1) #마지막으로 남은 수에 대하여 1씩 빼기
# print(count)
# -------------------------------------------------------------

# data = input()
# result = int(data[0])
# for i in range(1, len(data)):
#     num = int(data[i])
#     if num <= 1 or result <= 1:
#         result += num
#     else:
#         result *= num
# print(result)
# -------------------------------------------------------------
import sys
N = int(input())
data = list(map(int, sys.stdin.readline().split()))
data.sort()
result = 0 # 총 그룹의 수
count = 0 # 현재 그룹에 포함된 모험가의 수
for i in data: # 공포도 낮은 순으로 확인
    count += 1 # 현재 그룹에 해당 모험가 포함
    if count >= i: # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면, 그룹 결성
        result += 1 # 총 그룹의 수 증가시키기
        count = 0 # 현재 그룹에 포함된 모험가의 수 초기화
print(result)
