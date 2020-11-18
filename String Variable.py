#defining string variables
greet="Hello! How are you? "
print(greet)    #printing string variable
print(greet + "Hope you are good.")     #printing variable with some extra string

# SPLIT
wish=greet
print(wish.split(" ")[0]) #here the desired word is printed with the help of string
print("Good:Great:Fine".split(":")[0])

print(greet+"Good:Great:Fine".split(":")[0])