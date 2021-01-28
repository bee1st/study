a = 1
for i in range(3):
    a *= int(input())
a = str(a)
result = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for n in list(a):
    result[int(n) - int('0')] += 1

# while (True):
#     result[a % 10] += 1
#     a = a // 10
#     if a == 0:
#         break

for i in range(10):
    print(result[i])
