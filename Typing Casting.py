#Typing Casting
i=104
s="104"
print(i)    #104
print(s)    #104
print(type(s))  #<class 'str'>

'''
print(i+s) ||  This will give error as if 'i' is integer and 's' is string 

'''

#To do the previous print possible we need to do TYPE CASTING
s=int(104)
print(i+s)  #here the variable is converyed to integer  :- 208

#Type Casting to string
i=str(104)
s="104"
print(i+s)  #adding strings append them :- 104104

#Type Casting to float
i=float(104)
print(i)    #104.0
