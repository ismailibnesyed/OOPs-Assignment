
class Person():
    def __init__(self, name, age, money):
        self.name = name
        self.age = age
        self.money = money

class Men(Person):
    def __init__(self, name, age, money, height):
        self.height = height
        super().__init__(name, age, money)
    
    # Overload for Plus (+)
    def __add__(self,other):
        return self.money + other.money
    
    # Overload for Multiplication (*)
    def __mul__(self, other):
        return self.age * other.age
    
    # Overload for Substraction (-)
    def __sub__(self, other):
        return self.money - other.money

Rahim = Men('Abdur Rahim', 22, 5800, 65)
Karim = Men('Abdul Karim', 21, 7000, 64)

print(Rahim + Karim)
print(Rahim * Karim)
print(Rahim - Karim)



        