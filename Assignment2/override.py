
class Person():
    def __init__(self, name, age, money):
        self.name = name
        self.age = age
        self.money = money

    def eat(self):
        print(f'{self.name} eating Bread')

    def excercise(self):
        print('Walking')


class Men(Person):
    def __init__(self, name, age, money, height):
        self.height = height
        super().__init__(name, age, money)

    # Override
    def eat(self):
        print('Burger, Kaschi, BBQ')
    def excercise(self):
        print('Go to GYM')
    

Rahim = Men('Abdur Rahim', 22, 5800, 65)
Karim = Men('Abdul Karim', 21, 7000, 64)

Rahim.eat()
Karim.excercise()



        