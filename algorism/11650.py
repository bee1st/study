# arr = [[3, 4],
# [1, 1],
# [1, -1],
# [2, 2],
# [3, 3]]

# N = len(arr)

# # 0부터 9까지
# for i in range(N):
#     for j in range(N - i - 1):
#         if arr[j][0] > arr[j+1][0]:
#             arr[j], arr[j + 1] = arr[j + 1], arr[j]
#         elif arr[j][0] == arr[j+1][0]:
#             if arr[j][1] > arr[j+1][1]: 
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]         
# print(arr)


import sys
n = int(sys.stdin.readline())
arr = []
for i in range(n):
    a, b = map(int, input().split())
    arr.append([a, b])

for i in range(len(arr)-1):
    for j in range(i + 1, len(arr)):
        if arr[i][0] > arr[j][0]: 
            arr[i], arr[j] = arr[j], arr[i]
        elif arr[i][0] == arr[j][0]:  
            if arr[i][1] > arr[j][1]:
                arr[i], arr[j] = arr[j], arr[i]
for i in range(len(arr)):
    print(arr[i][0],arr[i][1])




# import sys
# N = int(input())
# arr = [] # 배열 선언
# for i in range(N):
#     a, b = map(int, input().split()) # (a, b) 입력받는 코드
#     arr.append([a,b]) # (a, b)를 차례대로 arr 배열에 넣어준다
#     # print(arr)
# arr.sort() # [[a1, b1], [a2, b2], ...] 를 정렬하는 코드
# for i in range(N): #입력받은 횟수만큼 반복
#     print(arr[i][0], arr[i][1])