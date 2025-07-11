from Modules.Authentication import authentication
from Modules.ProductManagement import ProductManagement
from Modules.SubModules.products_printer import product_printer

user_enter_way = int(input("1.Login  2.Signup ? "))

auth_result = None

if user_enter_way == 1:
    login_email = input("Enter Your Email : ")
    login_password = input("Enter Your PassWord : ")
    auth_result = authentication("login", login_email, login_password)
elif user_enter_way == 2:
    signup_user_name = input("Please Enter UserName : ")
    signup_email = input("Please Enter Email : ")
    signup_password = input("Please Enter Password : ")
    auth_result = authentication(
        "signup", signup_email, signup_password, signup_user_name)
else:
    print("Invalid Method!!")


if auth_result == True:
    user_cart = ProductManagement()
    
    print("Your Cart : ")
    for cart_item in user_cart:
        product_printer(cart_item)
        
    

elif auth_result == False:
    print("Please Login Or Signup!!")
