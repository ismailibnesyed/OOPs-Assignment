class Student:
    def __init__(self, name, age):
        self.__name = name    
        self.__age = age

    # Getter
    def get_name(self):
        print(f'{self.__name} is {self.__age} years old.') 

    # Setter
    def set_age(self, age):
        if age > 0:
            self.__age = age
            print(f'{self.__name} is {self.__age} years old.')
        else:
            print("Invalid age")

s1 = Student("Ruddro", 16)

# Getter
s1.get_name()

# Setter
s1.set_age(20)
