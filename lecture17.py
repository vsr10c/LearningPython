import  sys

varDrinkNum = input("Choose your drink"
                    "1.Water = $1.00"
                    "2.Cola = $1.50"
                    "3.Gatorade = $2.00")

varDrinkNumInt = int(varDrinkNum)

if varDrinkNumInt == 1:
    print("your choise is %s and the price is $%f"%("Water", 1.00))

elif varDrinkNumInt == 2:
    print("Your Choise is %s and the price is $%f"%("Cola", 1.50))
elif varDrinkNumInt == 3:
    print("your choise is %s and the price is $%f"%("Gatorade", 2.00))
else:
    print("Enter vaid input")
    sys.exit()