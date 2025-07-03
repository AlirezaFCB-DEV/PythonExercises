name = input("Please Inter YourName: ")
age = int(input("Please Enter YourAge : "))

if name == "Alireza" and age == 17 :
    print("Is Owner")
elif name not in {"alireza" , "dev" ,  "js"} or age not in {16 , 17 , 18} : 
    print("Is User")
    
    