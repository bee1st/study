TestCase = int(input())
for i in range(TestCase):
    a = input()
    b = []
    c = 0
    sum = 0
    b.append(a)
    for j in b:
        if j == 'O':
            c += 1
            sum += c
        else :
            c = 1
    print(sum)



    