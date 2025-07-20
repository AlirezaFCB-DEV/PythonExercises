list1 = [1, 2, 3]

it = iter(list1)

print(next(it))
print(next(it))


class Nums:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x


num2 = Nums()

