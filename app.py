class Person:
    x = 12

    def __init__(self, name, age):
        self.name = name
        self.age = age


a = Person("Alireza", 16)
b = Person("Mojtaba", 47)

a.x = "jsjsjs"

b.x = "TsTsTsTs"

print(a)
print(b)
print(a.x)
print(b.x)
