# String Merhods Review

# print the lenght of a string "Manchester United"
varStr = "Manchester United"
varStrLen = len(varStr)
print("String Length=", varStrLen)

# convert int 1234 to string and then access and print "3" from the new string
varIntOne = 1234
varStrOne = str(varIntOne)
print(varStrOne[2])

# use .upper() to make all the characters in the string "albania" upper case and print it in all capital
varStrTwo = "albania"
varStrTwoCon = varStrTwo.upper()
print(varStrTwoCon)

# use .lower() to make all the characters in the string "BELGIUM" lowercase and print the new string
varStrThree = "BELGIUM"
varStrThreeCon = varStrThree.lower()
print(varStrThreeCon)