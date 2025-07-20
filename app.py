class Flyer:
    def fly(self):
        print("i can fly!")


class Swimmer:
    def swim(self):
        print("i can swim!")


class duck (Flyer, Swimmer):
    pass


a = duck()

a.fly()
a.swim()
