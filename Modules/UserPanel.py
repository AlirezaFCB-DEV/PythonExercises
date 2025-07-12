from .ProductManagement import ProductManagement
from .SubModules.products_printer import product_printer

def user_panel () :
    
    user_cart = ProductManagement()
    
    print("Your Cart : ")
    for cart_item in user_cart:
        product_printer(cart_item)