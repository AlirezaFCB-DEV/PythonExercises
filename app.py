# try : 
#     print("salam")
# except ValueError :
#     print("value is invalid")
# except TypeError :
#     print("type is invalid")

############

try :
    print("code ...")
except (ValueError , TypeError) as e :
    print(f"Handled Error : {e}")
    