from Modules.Data.Products import products
from .SubModules.products_printer import product_printer


def buy_product():
    user_cart = []

    print("Welcome To My Shop! \nYou Can Choose Products Of This Products: ")

    for product in products:
        product_printer(product)

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

    return user_cart
