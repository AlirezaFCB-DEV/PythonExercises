def outer():
    x = "enclosing"

    def inner():
        x = "local"
        print(x)  # ! local scope

    inner()
    print(x)  # ! enclosing scope


x = "global"

outer()

print(x)  # *global

# print() #len() #... #! Built-in scope
