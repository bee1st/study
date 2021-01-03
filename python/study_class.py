class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self, to_name):
        print("안녕!"+ to_name + "나는" + self.name)
    
    def introduce(self):
        print("내이름은 " + self.name + " 그리고 나는 " + str(self.age) + "살이야")

woony = Person("우니", 20)
woony.introduce()


