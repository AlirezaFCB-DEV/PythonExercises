from Modules.Authentication import authentication
from Modules.UserPanel import user_panel
from Modules.OwnerCMS import owner_cms
from Modules.AdminCMS import admin_cms

user_enter_way = int(input("1.Login  2.Signup ? "))

auth_result = None


match (user_enter_way):
    case 1:
        login_email = input("Enter Your Email : ")
        login_password = input("Enter Your PassWord : ")
        auth_result = authentication("login", login_email, login_password)
    case 2:
        signup_user_name = input("Please Enter UserName : ")
        signup_email = input("Please Enter Email : ")
        signup_password = input("Please Enter Password : ")
        auth_result = authentication(
            "signup", signup_email, signup_password, signup_user_name)
    case (_):
        print("Invalid Method!!")


match (auth_result):
    case "owner":
        owner_cms()
    case "admin":
        admin_cms()
    case "user":
        user_panel()
    case _:
        print("Please Login Or Signup!!")
