with open("script.js", "w") as f:
    f.write("let x = 21")
    f.writelines(["\n", "let j = 'ssd'", "\n",
                 """const btn = document.querySelector("button")"""])

with open("script.js", "r") as f:
    all_data = f.read()

    print(all_data)

with open("script.js", "r") as f:
    one_line = f.readline()
    print(one_line)

with open("script.js", "r") as f:
    lines_list = f.readlines()
    print(lines_list)

# secondary parameters of open : 
# r = just read
# w = just write and clear file
# a = add end of file
# x = create file if have file return error
# r+ = read and write 
# b = binary
# t =  text mode is default
# rb = reade a binary file like img 
# a+ = read and add
#wb =  save binary like download files