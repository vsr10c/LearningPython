"""# Addition funcation
varNumone = input("Enter number one:")
varNumTwo = input("Enter number two:")
varInPut = input("Select operation:")
varNumOneCon = int(varNumone)
varNumTwoCon = int(varNumTwo)

def add(a, b):
    c = a + b
    return c

def sub(a, b):
    c = a - b
    return c

if varInPut == "+":
    print(add(varNumOneCon, varNumTwoCon))
    print("C value is:%s" %(add(varNumOneCon, varNumTwoCon)))
elif varInPut == "-":
    print(sub(varNumOneCon, varNumTwoCon))
    print("C value is:%s" %(sub(varNumOneCon, varNumTwoCon)))
else:
    print("Select proper operation")

"""

"""
Single parameter and zero parameter functions:
1.define a function that takes no parameters and prints a string
2.create a variable and assign it the value 5
3.create a function that takes a single parameter and prints it
4.call the function you created in step 1
5.call the function you created in step 3 with the variable you made in step 2 as its input
"""
# ----------------------------------------------------------------------------------------------------------------------
def firstFun():
    print("This is a test funcation")

varNum = 5

def singVar(a):
    print("Funcation parameter is:", a)

firstFun()
singVar(varNum)


# ----------------------------------------------------------------------------------------------------------------------
"""
multiple parameter functions:
1.create 3 variables and assign integer values to them
2.define a function that prints the difference of 2 parameters
3.define a function that prints the product of the 3 variables
4.call the function you made in step 2 using 2 of the variables you made for step 1
5.call the function you made in step 3 using the 3 variables you created for step 1
"""
# ----------------------------------------------------------------------------------------------------------------------
varOne = 1
varTwo = 2
varThree = 3

def defr(a,b):
    c = a - b
    print("Difference is:", c)

def prod(a,b,c):
    d = a * b * c
    print("Product is:", d)

defr(varNum,varThree)
prod(varOne,varTwo,varThree)


# ----------------------------------------------------------------------------------------------------------------------
"""
Calling previously defined functions within functions:
1.create 3 variables and assign float values to them
2.create a function that returns the quotient of 2 parameters
3.create a function that returns the quotient of what is returned by the function from the second step and a
third
 parameter
4.call the function you made in step 2 using 2 of the variables you created in step 1. Assign this to a
variable.
5.print the variable you made in step 4
6.print a call of the function you made in step 3 using the 3 variables you created in step 1
"""
# ----------------------------------------------------------------------------------------------------------------------

varFOne = 1.23
varFTwo = 4.56
varFThr = 0.12

def mod(a,b):
    c = a / b
    return c

def modTwo(e,f):
    g = e / f
    return g

varQue = mod(varFOne,varFTwo)

print(mod(varFOne,varFTwo))

print(modTwo(varQue,varFThr))



# ----------------------------------------------------------------------------------------------------------------------