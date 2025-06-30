def shop(item, price=100, *args, **tags):
    print(
        f"item={item} , price={price} , tuple type : args=[{args}] , dictionary (obj) :  tags=[{tags}]")


shop("Boxing Gloves", 120, "limited Edition", True, oz=12, color="blue")
