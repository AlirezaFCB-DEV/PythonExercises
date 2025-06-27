words = ["Alireza", "Boxing", "Trading", "Programming"]

for w in words:
    print(w, len(w))

#! words.copy().items() A Copy Of Words Objects(Dictionary)

user = {"name": "Alireza", "id": 1, "age": 16, "job": "FrontEnd Developer"}

# user2 = user.copy().items() #! Copy OF User

# print(user2)

for property, value in user.copy().items():
    if value == "Alireza":
        print("1name")
        print(property)
    elif value == 16:
        print("3age")
        print(property)
    elif value == "FrontEnd Developer":
        print("4job")
        print(property)
    else:
        print("2id")
        print(property)

for prop in user:
    print(prop)

for prop, val in user.items():
    print(prop, val)

js = "js"

#! slice structure [start : stop : step]

print(js[::-1])


users = {"Alireza": "active", "Marzie": "inactive",
         "Mojtaba": "inactive", "Mostafa": "inactive", "Narges": "inactive"}

for prop, val in users.copy().items():
    if prop == "Mostafa" or prop == "Narges":
        del users[prop]

print(users)

Parents = {}

for prop, val in users.items():
    if val == "inactive":
        Parents[prop] = "active"

print(Parents)