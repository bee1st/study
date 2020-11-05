# 1회용 함수 (제너레이터)
# 인덱스 몇번째인지 확인하기 enumerate
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

reversed_a = reversed(a)
for i in reversed_a:
    print(i, end = " ") # 9 8 7 6 5 4 3 2 1 0
print()
for i in reversed_a:
    print(i, end=" ") # reversed는 1회용 함수
print("*" * 30)

for i in reversed(a):
    print(i, end=" ")
print()
for i in reversed(a):
    print(i, end =" ")


a = [103, 56, 678, 43, 156]
enumerate_a = enumerate(a)
print(list(enumerate(a)))
for (i, element) in enumerate_a:
    print("{}번째 요소는 {}입니다.".format(i, element))
print("*" * 40)
for (i, element) in enumerate_a:
    print("{}번째 요소는 {}입니다.".format(i, element)) #enumerate도 1회용 함수

a = {"key_1" : "value_1", "key_2" : "value_2","key_3" : "value_3","key_4" : "value_4"}
for key, value in a.items():
    print("{}키의 값은 {}입니다.".format(key,value))

#리스트 내포
array = []
for i in range(0, 20, 2):
    array.append(i * i)
print(array)
print("*" * 100)
array = [i * i for i in range(0, 20, 2)]
print(array)

array_ex = [i for i in range(10) if i % 3 == 0]
print(array_ex)

#연습문제
output = 0
for i in range(1, 100 + 1):
    if "{:b}".format(i).count("0") == 1:
        print("{} : {:b}".format(i,i))
        output += i
print("합계 : {}".format(output))


output = [i for i in range(1, 100 + 1) if "{:b}".format(i).count("0") == 1]
for i in output:
    print("{} : {}".format(i, "{:b}".format(i)))
print("합계 : {}".format(sum(output)))