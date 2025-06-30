def show (name , age , city):
    print(f"{name} is {age} years old living in {city}")
    
info = {"name" : "Alireza" , "age" : 16 , "city" : "karaj"}
show(**info)