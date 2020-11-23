# 함수 정의 방법
# def function_name(parameter):
#   code

# 함수 호출
# 함수명(parameter)

# 함수 선언 위치 중요
# 예제 1
def hello(world):
    print("hello ", world)

hello("python!")
hello(7777)

# 예제 2
def hello_return(world):
    val = "Hello" + str(world)
    return val

str = hello_return("python!!!!!")
print(str)

# 예제 3 (다중리턴)
def func_mul(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return y1, y2, y3

val1, val2, val3 = func_mul(100)
print(val1, val2, val3)

# 예제 4 (데이터 타입 반환)
def func_mul2(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return [y1, y2, y3] #리스트

lt = func_mul2(100)
print(lt)

# 예제 5 (데이터 타입 반환)
def func_mul3(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return (y1, y2, y3) #튜플

tu = func_mul3(100)
print(tu)

# 예제 6
# *args, *kwargs

def args_func(*args): #매개변수의 갯수를 모를때 사용 (타입:튜플)
    print(args) 

args_func('kim')
args_func('kim', 'lee')

def args_func2(*args):
    # for t in args:
    #     print(t)
    for i, v in enumerate(args): #번호 매길때 사용
        print(i, v)

args_func2('kim', 'lee', 'yang')

def kwargs_func(**kwargs):
    for k, v in kwargs.items():
        print(k, v)

kwargs_func(name1 = 'kim', name2 = 'lee', name3 = 'yang')

# 전체 혼합
def example_mul(arg1, arg2, *args, **kwargs):
    print(arg1, arg2, args, kwargs)

example_mul(10, 20)
example_mul(10, 20, 'park', 'yang', age1 = 24, age2 = 44)

#중첩함수(클로저)
def nested_func(num): #1 10000
    def func_in_func(num): #2 10000 #5 20000
        print(num) #6 20000 출력
    print("in function") #3 in function 출력
    func_in_func(num + 10000) #4 10000 + 10000

nested_func(10000) 

#예제 7
def func_mul3(x : int) -> list:
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return [y1, y2, y3] 

print(func_mul3(5))

