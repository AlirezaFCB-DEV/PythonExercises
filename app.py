from Modules.Data.Products import products
from Modules.Authentication import authentication

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
    print("Welcome To My Shop! \nYou Can Choose Products Of This Products: ")

    for product in products:
        print(
            f"{product['id']}.{product['name']} | Price:{product['price']} | count:{product['count']} \n")
elif auth_result == False:
    print("Please Login Or Signup!!")
