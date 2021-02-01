def d(n):
    sum = n
    n = str(n)
    for i in range(len(n)):
        sum += int(n[i])
    return sum

check = [False for i in range(10001)]

for i in range(1, 10000):
    if d(i) < 10001:
        check[d(i)] = True

for i in range(1, 10000):
    if check[i] == False:
        print(i)
