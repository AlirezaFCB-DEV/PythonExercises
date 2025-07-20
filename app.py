class Person :
    def __init__(self, name):
        self.__name = name #! Private Variable
        
    def get_name (self):
        return self.__name
    
Ali = Person("Alireza")

print(Ali.get_name())
print(Ali.__name)