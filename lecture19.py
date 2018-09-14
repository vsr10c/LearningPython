varUName = input("Enter your name:")

varUNameLen = len(varUName)

if varUNameLen < 4:
    print("Your name is less than 4 letters.")
elif varUNameLen <= 10:
    print("Your name is at least 4 letters but less than 10 letters.")
else:
    print("Your name is very long.")
exit()