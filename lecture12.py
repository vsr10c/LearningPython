"""
String Concatenation:
1.create a variable and assign it the phrase "hello world" by concatenating the strings "hello" and " world"
2.create a variable and assign it the integer 11
3.create a variable and assign it the integer 38
4.create a variable and use the variables from steps 2 and 3 and string concatenation to assign it the string
"1138"
"""
# type your code for "String Concatenation" below this comment and above the one below it.
varCatStrOne = ("Hello!" + " " + "World")
print(varCatStrOne)

varIntOne = 11
varIntTwo = 38

varCatStrTwo = (str(varIntOne)+str(varIntTwo))
print(varCatStrTwo)
# ----------------------------------------------------------------------------------------------------------------------
"""
%s and input():
1.create a variable to hold a user's favorite restaurant (use input() for this.)
2.create a variable to hold the name of a place a user wants to visit.
3.create a variable to hold the user's nickname or first name if they don't have a nickname.
4.use the %s operator to assign the string "Your favorite restaurant is [name of favorite restaurant], you want
to visit1
 [name of place the user wants to visit], and your nickname or first name is [nickname or first name]" to a
variable
5.print that variable
"""
# type your code for "%s and input()" below this comment and above the one below it.

varFavRes = input("What is your favorite restaurant?")
varFavPlc = input("What is your favorite place to visit?")
varUsrName = input("What is your name?")

print("Your favorite restaurant is %s, you want to visit %s, and your name is %s." % (varFavRes, varFavPlc, varUsrName))