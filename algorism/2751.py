import sys
N = int(sys.stdin.readline())
sort1 = [] # 넣어줄 리스트 생성

for i in range(N):
    n = int(sys.stdin.readline())
    sort1.append(n) # 입력한 숫자 하나씩 sort1 에 넣어주기

for j in sorted(sort1): # sort1 리스트 정렬
    print(j) #[j] 번호만큼 하나씩 뽑아서 출력
