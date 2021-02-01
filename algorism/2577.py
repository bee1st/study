A = int(input())
B = int(input())
C = int(input())

Result = str(A * B * C)

count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for n in list(Result):
    count[int(n)] += 1

# while (True):
#     result[a % 10] += 1
#     a = a // 10
#     if a == 0:
#         break

for i in range(10):
    print(count[i])
