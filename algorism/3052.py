b = []
for i in range(10):
    a = int(input())
    b.append(a % 42)

a = len(set(b))
print(a)