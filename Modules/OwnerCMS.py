from .accesses import owner_accesses
from .SubModules.show_accesses import show_accesses

def owner_cms () :
    show_accesses("owner" , owner_accesses)
    owner_access = input("For An Access Please Call With Name : ")
    match owner_access :
        case "POST" : 
            do_POST()
        case "GET" :
            do_GET()
        case "PUT" :
            do_PUT()
        case "DELETE" :
            do_DELETE()
        case _ :
            print("Invalid Method!!")