import sys
b = str(input())
count = 0
for i in b:
    if i == '(':
        count += 1
    elif i == ')':
        count -= 1
if count == 0:
    print('YES')
else :
    print('NO')