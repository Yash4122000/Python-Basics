# LIST
'''
List is a variable in which different type of elements can be stored deperated with commas.
List is mutable in nature wiz. the elements can be change once the list is formed.
List has Variable length.
'''
l=['a','b','c','d','1','2','3','4']
print(l)    #['a', 'b', 'c', 'd', '1', '2', '3', '4']
print(l[5])     #2
print(l[-4])    #1
print(l[:])     #['a', 'b', 'c', 'd', '1', '2', '3', '4']
print(l+['X','Y','Z'])  #['a', 'b', 'c', 'd', '1', '2', '3', '4', 'X', 'Y', 'Z']
l[3:5]=['#','%']        
print(l)        #['a', 'b', 'c', '#', '%', '2', '3', '4']
l[3:4]=[]
print(l)        #['a', 'b', 'c', '%', '2', '3', '4']

#Length of List

print(len(l))   #7

m=['A','B','C','D','!','@','#','$']
n=[l,m]
print(n)        #[['a', 'b', 'c', '%', '2', '3', '4'], ['A', 'B', 'C', 'D', '!', '@', '#', '$']]
