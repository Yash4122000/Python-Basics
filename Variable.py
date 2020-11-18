print("Hello!") #simple string printing

print(5) #print a number; doesn't requires the double inverted commas{ " " }

#defining integer variables and having matematical operations
num1=10
num2=20
print(num1+num2)

#defining float variable
x=5.5
y=5.5
print(x+y)
print(x*y)
print(x*y+y*x)

#defining string variables
greet="Hello! How are you? "
print(greet)    #printing string variable
print(greet + "Hope you are good.")     #printing variable with some extra string

# SPLIT
wish=greet
print(wish.split(" ")[0]) #here the desired word is printed with the help of string
print("Good:Great:Fine".split(":")[0])

print(greet+"Good:Great:Fine".split(":")[0])

