# 1부터 시작 이웃하는 방에 들어갈때 +1
# 13까지는 3 58까지는 5
# 1 - 1  1
# 2 ~ 7 - 6  2
# 8 ~ 19 - 12 3
# 20 ~ 37 - 18 4
# 39 ~ 61 - 24 5

room = 1
start = 1
plus = 6
number = int(input())
if number == 1:
    print(1)
else :
    while True:
        start += plus
        room += 1
        if start >= number:
            print(room)
            break
        plus += 6




