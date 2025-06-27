userNum = int(input("Please Enter A Number : "))

print("UserNum : ", userNum)

studentScore = float(input("Please Enter Your Score : "))

if studentScore <= 10:
    print("Your Not Success , Your Degree D :((")
elif studentScore <= 13:
    print("Your Degree C")
elif studentScore <= 17:
    print("Your Degree B")
else:
    print("Your Degree A")
