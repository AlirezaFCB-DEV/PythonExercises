def show_accesses(admin_type , accesses_list):
    print(f"Welcome {admin_type} !")
    accesses = ""
    for access in accesses_list:
        accesses += f"{access} "

    print(f"You Can Do This Accesses : {accesses}")
