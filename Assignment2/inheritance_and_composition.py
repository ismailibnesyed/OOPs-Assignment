# inheritance

class Animal:
    def sound(self):
        print('Sound makes by animal')

class Dog(Animal):
    def dog_sound(self):
        print('Dog makes ghew ghew sound')

d = Dog()

d.sound()
d.dog_sound()

# Composition

class Engine:
    def start(self):
        print('Engine start now: ')

class Car:
    def __init__(self):
        self.engine = Engine() # Composition
    
    def drive(self):
        self.engine.start()
        print('Car is starting now')

c = Car()
c.drive()
