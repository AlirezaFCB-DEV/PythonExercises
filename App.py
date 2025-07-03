basket = {"LapTop" , "Mog" , "KeyBoard" , "Boxing Glows" , "Boxing Band"}

print(type(basket))
print(basket)

print("Js" in basket)
print("Boxing Glows" in basket)

#################

a = set("jst")
b = set("react")

print(a - b) #! Items that are in a but not in b
# print(a | b)
print(b | a) #! their community
print(a & b) #! Shared Item
print(a ^ b) #! Just In One Sets