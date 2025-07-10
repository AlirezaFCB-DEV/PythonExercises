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
    user_cart = []

    print("Welcome To My Shop! \nYou Can Choose Products Of This Products: ")

    for product in products:
        print(
            f"{product['id']}.{product['name']} | Price:{product['price']} | count:{product['count']} \n")

    print("For End Buying 0+Enter")

    def select_product():
        return int(input("Please Enter A Product Id For Buy A Product : "))

    def new_product(name, price, id, count=1):
        return {
            "id": id,
            "name": name,
            "price": price,
            "count": int(count)
        }

    while (True):
        selected_product = select_product()
        if selected_product == 0:
            break
        else:
            for product in products:
                if product["id"] == selected_product:
                    product_index = product["id"] - 1
                    main_product = products[product_index]
                    product_count = input(
                        "Please Enter Product Count [Default = 1]: ")
                    if product_count:
                        user_cart.append(new_product(
                            main_product["name"], main_product["price"], main_product["id"], count=product_count))
                    else:
                        user_cart.append(new_product(
                            main_product["name"], main_product["price"], main_product["id"]))

    print(user_cart)

elif auth_result == False:
    print("Please Login Or Signup!!")
