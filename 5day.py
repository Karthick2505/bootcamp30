#Write a program to create a list of n integer values and do the following
#Add an item in to the list (using function)
#Delete (using function)
#Store the largest number from the list to a variable
#Store the Smallest number from the list to a variable

list=[10,20,30,40,50,60,70,80,90,100]
print("The list is",list)
largenum = max(list)
print("The largest number is",largenum)
smallnum = min(list)
print("The smallest number is",smallnum)
b = list.append(200)
print("The list after appending",list)
list1 = ['A' ,'B','C','D']
del list1[2]
print("The list after deletion",list1)

#Create a tuple and print the reverse of the created tuple
tuple = (1, 2, 3 , 5,7,9)
print("The initial tuple is",tuple)
new = sorted(tuple,reverse = True)
print("The reversed tuple is",new)

#Create a tuple and convert tuple into list
tuple = (1, 2.7, 'hello' , 'karthi' , 55, 20)
print("tuple is",tuple)

list_new = list(tuple)
print("List is",list_new)
