class Student:

    def __init__(self, name):
        self.name = name

    @staticmethod
    def multiply(a, b):
        result = a * b
        print(result)

    @classmethod
    def amni(cls, name):
        print(f'{name} meyeder piche ghur ghur kore')


Student.amni('Ruddro')
Student.multiply(2, 8)