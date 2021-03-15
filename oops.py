class Animal:
    def __init__(self, type, age):
        self.type = type
        self.age = age
        
a = Animal('dog',12)
print(f'{a.type}, {a.age}')
print(a.__dict__)
