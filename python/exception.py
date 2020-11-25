# 예외처리의 이해

# 예외종류
# 문법적으로 에러가 없지만, 
# 코드 실행(런타임)프로세스에서 발생하는 예외처리도 중요
# linter : 코드 스타일, 문법 체크

# SyntaxError : 잘못된 문법

# print('Test) #SyntaxError: EOL while scanning string literal
# if True  #SyntaxError: invalid syntax
# x => y


# NameErorr : 참조변수 없음
a = 10
b = 15
# print(c) #NameError: name 'c' is not defined

# ZeroDivisionError : 0 나누기 에러
# print(10 / 0) #ZeroDivisionError: division by zero

#IndexError : 인덱스 범우 ㅣ오버
x = [10, 20, 30]
# print(x[3]) #IndexError: list index out of range

# keyError
dic = {"name" : 'kim', 'age' : 33, 'city' : "seoul"}
# print(dic['hobby']) #KeyError: 'hobby'
print(dic.get('hobby')) #None 출력

# AttributeError : 모듈, 클래스에 있는 잘못된 속성 사용시 예외
import time
print(time.time())
# print(time.month()) #AttributeError: module 'time' has no attribute 'month'

# ValueError : 참조값이 없을때 발생
x = [1, 5, 9]
# x.remove(10) #ValueError: list.remove(x): x not in list
# x.index(10) #ValueError: 10 is not in list

# FileNotFoundError
# f = open('test.txt', 'r') #FileNotFoundError: [Errno 2] No such file or directory: 'test.txt'

# TypeError
x = [1, 2]
y = (1, 2)
z = 'test'
# print(x + y) #TypeError: can only concatenate list (not "tuple") to list
# print(x + z) #ypeError: can only concatenate list (not "str") to list

