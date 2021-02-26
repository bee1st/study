# n 범위 500 => o(n**3)
# n 범위 2000 => o(n**2)
# n 범위 100,000 => o(NlogN)
# n 범위 10,000,000 => o(N)
# -------------------------------------------------------------
import time
start_time = time.time() #측정 시작
'''
# 프로그램 소스코드
'''
end_time = time.time() #측정 종료
print('time : ', end_time - start_time) #수행 시간 출력
# -------------------------------------------------------------
n = 4
m = 3
arr = [[0] * m for _ in range(n)]
print(arr)
# -------------------------------------------------------------
# append() -> o(1)
# sort()  -> 변수명.sort() 오름차순 o(NlogN)
#         -> 변수명.sort(reverse = True) 내림차순 o(NlogN)
# reverse() -> 변수명.reverse() 리스트 원소의 순서를 모두 뒤집어 놓는다 o(N)
# insert() -> insert(삽입 위치 인덱스, 삽입값) o(N)
# count() -> 변수명.count(특정 값) 특정 값을 갖는 데이터 갯수 셀때 o(N)
# remove() -> 변수명.remove(특정 값) 특정 값을 갖는 원소를 제거, 여러개면 한개만 제거 o(N)
# -------------------------------------------------------------
data = set([1, 1, 2, 3, 4, 4, 5]) #중복 제거
print(data)
data = {1, 1, 2, 3, 4, 4, 5}
print(data)
# -------------------------------------------------------------
a = set([1, 2, 3, 4, 5])
b = set([3, 4, 5, 6, 7])
print(a | b) # 합집합
print(a & b) # 교집합
print(a - b) # 차집합
# -------------------------------------------------------------
data = set([1, 2, 3])
data.add(4) # 새로운 원소 추가
data.update([5, 6]) # 새로운 원소 여러개 추가
data.remove(3) #특정 값 갖는 원소 삭제
print(data)
# -------------------------------------------------------------
# a = list(map(int, input().split()))
# a, b, c = map(int, input().split())
# sys.stdin.readline().rstrip() --> 문자열 입력받기
# -------------------------------------------------------------
# 파이썬 3.6이상
answer = 8
print(f"정답은 {answer}입니다.")
# -------------------------------------------------------------
# x in 리스트 -> 리스트 안에 x가 들어있을때 참
# x not in 문자열 -> 문자열 안에 x가 들어가 있지 않을때 참
# -------------------------------------------------------------
# 서로다른 n개에서 서로다른 r개를 선택하여 일렬로 나열
# 순열 : n * (n - 1) * (n - 2) * ... * (n - r + 1)
from itertools import permutations
data = ['A', 'B', 'C']
result = list(permutations(data, 3))
print(result)
# 중복 순열
from itertools import product
data = ['A', 'B', 'C']
result = list(product(data, repeat = 3))
print(result)
# -------------------------------------------------------------
# 서로다른 n개에서 순서에 상관없이 서로 다른 r개를 선택
# 조합 : n * (n - 1) * (n - 2) * ... * (n - r + 1) / r!
from itertools import combinations
data = ['A', 'B', 'C']
result = list(combinations(data, 2))
print(result)
# 중복 조합
from itertools import combinations_with_replacement
data = ['A', 'B', 'C']
result = list(combinations_with_replacement(data, 2))
print(result)
# -------------------------------------------------------------
# 내부 원소 카운트
from collections import Counter
counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])
print(counter['blue'])
print(counter['green'])
print(dict(counter))
# -------------------------------------------------------------
# 최대공약수
import math
def lcm(a, b):
    return a * b // math.gcd(a, b)
a = 21
b = 14
print(math.gcd(21, 14)) #최대 공약수(GCD) 계산
print(lcm(21, 14)) #최소 공배수(LCM) 계산
# -------------------------------------------------------------

