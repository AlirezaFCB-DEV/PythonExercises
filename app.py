file = open("info.txt", "w")
file.write("Hello Is A Test MSG!! \n")
file.close()

file = open("readme.md", "r")
print(
    file.read()

)
file.close()

#####################

with open("js.js", "w") as f:
    f.write("console.log('hahahaha')")

with open("js.js", "r") as f:
    data = f.read()
    print(data)
