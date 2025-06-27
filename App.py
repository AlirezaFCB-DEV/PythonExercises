for i in range(10):
    print(i + 1)

for i in range(5, 10):
    print(i)

for i in range(0, 10, 3):
    print(i)

for i in range(-1, -100, -10):
    print(i)

alireza = "alireza"

for w in alireza:
    print(w)

words = ["alireza", 15, "js", "react", 18, ["js", "angular", "react"]]

for i in range(len(words)):
    print(i, words[i])

print(range(10))

print("line 25: ", sum(range(10)))
# print("line 26: ", sum(8)) #! error for that number is not iterable

