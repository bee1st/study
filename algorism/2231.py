import sys

N = list(map(int, sys.stdin.readline().split()))

check = False
for i in range(N[0]):
    number = i
    new_number = number
    while (number):
        new_number += number % 10
        number //= 10
    
    if N[0] == new_number:
        check = True
        print(i)
        break

if check == False:
    print(0)

