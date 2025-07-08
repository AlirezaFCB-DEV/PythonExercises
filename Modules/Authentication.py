
from .Data.Users import users


def authentication(method, email, password, user_name=""):
    """
    this func authenticate a user for login or signup!
    props: method: "signup or login" , email , username , password
    output: Boolean
    """
    if method == "login":

        for user in users:
            if email == user["email"] and password == user["password"]:
                print("Welcome To Your Account!")
                return True

            print("Email Or Password Incorrect!!")
            return False

    elif method == "signup":
        for user in users:
            if email == user["email"]:
                print("User Already Exists!")
                return False

        new_user = {"id": len(users) + 1, "name": user_name,
                    "email": email, "password": password}
        users.append(new_user)

        print("Welcome To Your Account!!")

        return True