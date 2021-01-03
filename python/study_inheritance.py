class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self, to_name):
        print("안녕!"+ to_name + "나는" + self.name)
    
    def introduce(self):
        print("내이름은 " + self.name + " 그리고 나는 " + str(self.age) + "살이야")

# Person 상속
class Police(Person):
    # 상속 안받을때 써야하는 코드
    # def __init__(self, name, age):
    #     self.name = name
    #     self.age = age 

    def arrest(self, to_arrest):
        print("넌 체포됐다 " + to_arrest)

# Person 상속
class Programmer(Person):
    def Program(self, to_program):
        print("다음엔 뭘 만들지? 아 이걸 만들자 " + to_program)
    
kim = Person("김씨", 20)
lee = Police("이씨", 21)
yang = Programmer("양씨", 22)

lee.introduce() # Person 상속받아서 
kim.introduce()
lee.arrest('kim')
yang.Program('게시판')

# yang.arrest('lee') yang은 Programmer 이기때문에 arrest못한다.