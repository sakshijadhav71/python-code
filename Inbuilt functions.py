#function()-function is a name given to a block of code with start executing when user involves it.

#1 Inbuilt function
#2 user-defined function


# for checking which function we used in which datatype----> dir('datatype')



#.........................STRING FUNTIONS....................................

# Inbuilt function for strings- 
#1 lower()- convert whole string in lower case.
#syntax var.lower()
#ex var="hello"
#var.lower()

#2 upper()- converts whole string in upper case.
#syntax- var.upper()

#3 swapcase- swap the uppercase character  into lowercase and lowercase in uppercase character.
#syntax- var.swapcase()

#4 index()- returns the index value.
#syntax- var.index()
# rindex()- returns the last occurans index
#syntax- var.rindex()

#5 find()- returns the first index occurance .
#syntax- var.find()
# rfind()- returns the last index occurance.
#diff b/w find and index - index function returns only var value but find function return all the index values


#### Inbuilt() for Boolean functions- which returns the value in true or false.

#1 isalpha()- when we have value in  alphabets it returns true value otherwise returns false.
#syntax- var.isalpha()

#2 isdigit()- returns thetrue when string have digit values. 
#syntax- var.isdigit()

#3 isspace()- returns the true when string have any space.
#syntax-var.space()
#ex- var=' '
# var.isspace()

#4 isalnum()- when we have alphanets in string its return true otherwise returns false.
#syntax- var.isalnum()

#5 split()- returns a list of splited character
#syntax- var.split()
#var="hello buddy how are you?"
# var.split('h',1)

#6 startswith()- check first character if first charcter is match then return trueotherwise returns false.
# var.starstwith()-

#7 endswith()- check endt character if first charcter is match then return trueotherwise returns false.
#syntax- var.endswith()

#8 strip()- removes extra and start(leading) and last(drailing) spaces from string.
# rstrip()- remove right space in the string
# lstrip()- remove left space in the string
#syntax-var.strip()
#var='    hello world    ' ---> 'helloworld

#9 enumerate()-enumarate function is used to bind the value of the collection with there index value and return
# your object addresss a containing all the tuples having index and value pair and to print the value from the 
# address you have to typecast
# syntax- list(enumerate(var))

#10 zip()-returns object
#syntax- list(zip(var))


#...........................................LIST FUNTIONs..................................................
#for insertion in a list
# 1 append()--->Add the values at the end of the list. Its only take single argument.
#syntax---> list.append(value)
# ex--> ls.append(100)

# 2 extend---> you can pass multiple values .its only take collection values.
# syntax---> ls.extend(values)
#ex-->ls.extend([100,200,300])
# 3 insert()--> if we want to add values at perticular position.
#syntax---> ls.insert(index,value)
#ex--> ls.insert(1,100)

#for deletion in a list
# 1 pop()-->remove the last or specific value
# syntax-->ls.pop()
#ex--> ls.pop(100)
# 2 del keyword--> is used to remove specific element or list.
# 3 remove()--> we have to write which value we want to remove.
#ls.remove(values)
#ex--> ls.remove(100)
#  4 clear()---> is used to remove whole list.
#syntax-->ls.clear(list)
#ex-->ls.clear()


# 5 index()--->is used to find the index
#syntax--> ls=[10,20,30]-->  ls.index(20)--=>o/p-->[10,30]
# 6 sort()--> used to give output in accsending order
##syntax-->ls.sort()
# decsending order--> ls.sort(reverse=True)
# 7 sorted--> used to sort the list but not change actual list.
# syntax--> sorted()
# 8 reverse()--> is used to reverse the list
# reversed--> is used to reverse the list but it will give output in index format.if we want output so we have to typecast it
# syntax--> list(reversed(ls))
# 9 enumerate()--> Enumarate function is used to bind the value of the collection with there index value and return
# your object addresss a containing all the tuples having index and value pair and to print the value from the 
# address you have to typecast
# EX-->lst= [10,20,30,40,50]
# print (tuple(enumerate(lst)))
# 10 zip()--> return object
#ex
# ls1=[10,20,30]
# ls2=[100,200,300]
# print(list(zip(ls1,ls2)))
# for i, j in zip(ls1 ,ls2):
#     print(i,j)   

#................................................TUPLE FUNTIONs...................................................
# 1 index()-->gives index value
# 2 count()--> count the values. 

#.......................................SET FUNCTIONS..........................................................

# set is mutable datatype but only accept immutable datatypes values.

#for adding values
# 1 add()--->whenever we want to add any value in set we used add()
# syntax--->var.add(value)
# 2 update()--> whenever we want to add collection values we used update()
# syntax--> var.update(collection values)

#for removing values
# 3 pop()---> pop function removes start value in set.
# syntax--->var.pop()
# 4 remove()--> when we want to remove a perticular value from set we used remove function.
# syntax--> var.remove(value)
# 5 discard()--> if we removing any value, is not present in set it doesnot give any error.
# syntax-->var.discard()
# 6 clear()--> remove all values and give output into empty set.  
# syntax-->var.clear()
#
# 7 union()--> is used to join two set 
# syntax--> var1.union(var2)
# 8 intersection--> is used to get same values in two set .
# syntax--> var1.intersection(var2)
# 9 intersection_update()--> stores the o/p of intersection in var1.
#syntax--> var1.intersection_update(var2)
# 10 difference--> remove match  elements from var1 and var2 and give the difference output
#syntax--> var1.difference(var2)
# 11 difference_update--> stores the output of difference in var1
# syntax--> var1.diiference_update(var2)
# 12 symmetric_difference--> its remove match values and give output into unmatched values set.
# syntax-->var1.symmetric_difference_update(var2)

# boolean methods
# 1 isdisjoint()--> true if both set have no common value 
# syntax--> var1.isdisjoint(var2)
# 2 issubset()--> check if all the elements of set2 is present in set1. if yes then gives true
# syntax-->var1.issubset(var2)
# 3 issuperset--> check if all the elements of set2 is present in set1
# syntex--> var1.issuperset(var2)
# a={1,2,3,4,5,6,7,8} b={1,2,3}--> a is superset and b is subset
















































































































































































































































































































































































































































































































































