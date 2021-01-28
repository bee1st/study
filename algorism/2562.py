a = []
b = []
for i in range(9):
    x = int(input())
    a.append(x)

# a가 입력받은 배열
b = sorted(a)

# count = 0
# for j in range(9):
#     if b[8] != a[j]:
#         count += 1
#     elif b[8] == a[j]:
#         count += 1
#         break

j = 0
for j in range(9):
    if b[8] == a[j]:
        break
    
print(b[8])
print(j + 1)
# print(count)