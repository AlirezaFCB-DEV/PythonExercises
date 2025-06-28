def say_hello (name) :
    print(f"Hello {name}")
    
say_hello("Alireza")

def sum (num1  , num2) :
    return num1 + num2

print(sum(51 , 73))

def user_info (name , age = 16 , city="Tehran"):
    print(name , age , city )
    
user_info("Alireza" , city="Karaj")

def greet (name = "Ghost") :
    print(name)

# greet()
greet("Alireza")

def x (*args) :
    print(args)

x(15 , "alireza" , True  , ["js" , "js"] , {"id" : 12})  