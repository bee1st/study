# dict_a = {}
# dict_a["name"] = "구름"
# print(dict_a)

# del dict_a["name"]
# print(dict_a)

# pets = [
#     {"name" : "구름", "age" : 5},
#     {"name" : "초코", "age" : 3},
#     {"name" : "아지", "age" : 1},
#     {"name" : "호랑이", "age" : 1},
# ]
# for pet in pets:
#     print("{} {}살".format(pet["name"], pet["age"]))


# numbers = [1,2,6,8,4,3,2,1,9,5,4,9,7,2,1,3,5,4,8,9,7,2,3]
# counter = {}
# for number in numbers:
#     if number in counter:
#         counter[number] += 1
#     else:
#         counter[number] = 1
# print(counter)


# character = {
#     "name" : "기사",
#     "level" : 12,
#     "items" : {
#         "sword" : "불꽃의검",
#         "armor" : "폴플레이트",
#     },
#     "skill" : ["베기", "세게 베기", "아주 세게 베기"]
# }

# for key in character:
#     if type(character[key]) is dict:
#         for k in character[key]:
#             print("{} : {}".format(k, character[key][k]))
#     elif type(character[key]) is list:
#         for item in character[key]:
#             print("{} : {}".format(key, item))

#     else:
#         print("{} : {}".format(key, character[key]))


# # import time
# # 처음 = time.time()
# # while 처음 + 5 >= time.time():  //5초후 프로그램 종료
# #     pass
# # print("프로그램이 종료되었습니다.") 


# i = 0
# while True:
#     print("{}번째 반복중입니다".format(i))
#     i += 1

#     input_text = input(">종료하시겠습니까?(y)")
#     if input_text in ["Y", "y"]:
#         print("반복을 종료합니다")
#         break

# numbers = [5, 15, 6, 20, 7, 225]
# for number in numbers:
#     if number < 10:
#         continue #현재 반복을 중지하고 다음 반복으로 넘어간다.
#     print(number)


# key_list = ["name", "hp", "mp", "level"]
# value_list = ["자바", 200, 300, 5]
# character = {}

# for i in range(len(value_list)):
#     character[key_list[i]] = value_list[i]
# print(character)


max = 0
a = 0
b = 0
for i in range(1, 99 + 1):
    j = 100 - i
    if max < i * j:
        max = i * j
print("최대가 되는 경우 : {} * {} = {}".format(i, j, max))

