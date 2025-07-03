users = ["Alireza", "Komeyl", "mojtaba", "Marzie"]

for index, value in enumerate(users):
    print(index, value)


names = ["Ali", "Sara"]
ages = [16, 18]

for name, age in zip(names, ages):
    print(f"{name} {age} years old")

for item in sorted(set("Banana")):
    print(item)

users2 = {"Alireza", "mojtaba", "zxa", "nh", "marzie", "komeyl"}

for item in sorted(users2):
    print(item)
