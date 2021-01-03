class Car:
    """Parent Class"""
    def __init__(self, tp, color):
        self.tp = tp
        self.color = color
    
    def show(self):
        return "I want a Car"

class Bmw(Car):
    """Sub Class"""
    def __init__(self, tp, color, price, brand ):
        super().__init__(tp, color)
        self.price = price
        self.brand = brand
    
    def show_model(self) -> None:
        return "Do you want it? : %s" % self.price

class Benz(Car):
    def __init__(self, tp, color, price, brand):
        super().__init__(tp, color)
        self.price = price
        self.brand = brand
    
    def show_model(self) -> None:
        return "Do you want it? : %s" % self.color

class Hyun(Car):
    def __init__(self, tp, color, price, brand):
        super().__init__(tp, color)
        self.price = price
        self.brand = brand
    
    def show_model(self) -> None:
        return "Korean Car : %s" % self.brand

    def show(self):
        return 'Car Info : %s %s %s %s ' %(self.tp, self.color, self.price, self.brand)
    
model1 = Benz('110', 'black', '20000$', 'germany')
model2 = Bmw('220', 'silver', '17000$', 'germany')
model3 = Hyun('330', 'white', '14000$', 'Korea')

print(model1.show_model())
print(model2.show_model())
print(model3.show())
print(model1.show())
print(model2.__dict__)

class x():
    pass
class y():
    pass
class z():
    pass
class a(x, y):
    pass
class b(y, z):
    pass
class c(a, b, z):
    pass
print(c.mro())
