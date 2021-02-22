N = input() #문자열 입력
a = [] # 리스트 생성
for i in N:
    a.append(i) #문자 하나씩 리스트에 추가
a = list(map(int, a)) #리스트 문자열을 숫자로 변환
a.sort(reverse=True) #내림차순 정렬
for i in a:
    print(i, end='') #엔터없이 출력