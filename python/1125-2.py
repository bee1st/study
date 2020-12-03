# class 클래스명 : 
#     함수
#     함수

# class Car:
#     def __init__(self, t, c):
#         print("생성자")
#         self.type = t
#         self.color = c
    
#     def showInfo(self):
#         print(self.type + ', ' + self.color)
    
#     def tunning(self, c):
#         self.color = c
#         self.showInfo()

#     def __del__(self):
#         print('소멸자')

# c1 = Car('suv', '은색')
# # c1.showInfo()
# c1.tunning('검은색')


class X(object):
    pass
class Y:
    pass
class Z():
    pass
print('상속관계 : ', X.mro())
print('상속관계 : ', Y.mro())
print('상속관계 : ', Z.mro())

# 너무 복잡한 다중상속은 코드 해석이 어려움
class A(X,Y):
    pass
class B(Y,Z):
    pass
class D(A,B,Z):
    pass
print('상속관계:',A.mro())
print('상속관계:',D.mro())

class Car:
    def __init__(self,type,color):
        self.type=type
        self.color=color
    def show(self):
        print('Car class show 메서드',self.type,self.color)

class KiaCar(Car):
    def __init__(self,carname,type,color):
        super().__init__(type,color)   # 부모생성자 호출
        self.carname=carname
    def show(self):
        print('KiaCar class show 메서드',self.type,self.color,self.carname)
    def tunning(self,color):
        self.color=color

class HyundaeCar(Car):
    def __init__(self,carname,type,color):
        super().__init__(type,color)   # 부모생성자 호출
        self.carname=carname

k1 = KiaCar('k9','세단','흰색')
k1.show()
k1.tunning('노랑')
k1.show()
print(k1.carname) # 객체 속성 접근

h1 = HyundaeCar('제네시스', '세단', '비둘기색')
h1.show()