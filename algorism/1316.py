def is_group_string(string):
    prev_char = ''
    focus = []
    for char in string:
        if prev_char != '' and prev_char != char:
            # 이전에 입력받은 게 있고, 이전 값과 다르고, 이전에 나온적이 있으면!
            if prev_char in focus:
                return False
            focus.append(prev_char)
        prev_char = char
    return True

a = int(input())
count = 0
for i in range(a):
    b = input()
    if is_group_string(b):
        count += 1
print(count)
