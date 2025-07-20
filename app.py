class Animal:
    def speak(self):
        print("This animal makes a sound")


class Dog(Animal):
    pass


a = Dog()

a.speak()


class Cat (Animal):
    def speak(self):
        print("meo")


b = Cat()

b.speak()
