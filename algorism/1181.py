N = int(input())
voca_list = []
for i in range(N):
    voca = str(input())
    voca_cnt = len(voca) #글자수
    voca_list.append((voca_cnt, voca))

voca_list = list(set(voca_list)) #중복제거
voca_list.sort()
for i in voca_list:
    print(i[1])