try :
    f = open("file.txt")
    #...
except FileNotFoundError:
    print("file not found!!")
finally :
    f.close() #! Always Running !!