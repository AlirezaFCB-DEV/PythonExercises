try :
    num1 = int(input("Please Enter A Number :"))
    print(100 / num1)
except ValueError :
    print("Please Enter Number !!")
except ZeroDivisionError :
    print("Don't Divide By Zero!")
    
try :
    num2 = int(input("Please Enter A Number : "))
    print(num2 * 5)
except Exception as e :
    print(f"Error: {e}")