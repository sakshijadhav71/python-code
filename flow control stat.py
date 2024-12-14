
# simple if


# 1  WAP to check that the given programming language is present inside the given list

# prog = eval(input('enter the languages  '))
# lang = input ('enter the language name :')
# if lang in prog :
#     print (lang)
#     print(f'{lang} is present')
# #     

# 2  WAP to check the number is even or not 

# n = int(input("enter the number: "))
# if n%2==0:
#  print (f"the number {n} is even")
#  print("even")
#  '''

# 3 WAP to check the number is odd or not

# a= int(input("enter the number:"))
# if a%2!=0:
#     print(f"the number {a} is odd")
# 

# 4 WAP to check the given no is divisible by 5
# a=int(input("enter the number:"))
# if a%5==0:
#     print(f"the number {a} divisible by 5")
#     

# 5 WAP to check that the given no is positive
# a = int(input("enter the number: "))
# if a>=0:
#     print (f"{a}the number is positive")
# 

#6 WAP to check the given string is pallindrome
# a = eval(input("enter the string"))
# if a[::][-1]:
#     print ("string is palindrome")
# 

#7  WAP to check that the first characcter of the given string is consonant

# a = eval(input("enter the string: "))
# if a[0] not in "aeiou" :
#     print("The first character of string is consonant")
# 

#8  WAP to cheack that the given value is string

# a = eval(input("enter the valur: "))
# if type(a)==str:
#     print ("the given value is string")
#     

#9  WAP to check that the number is divisible by 2 and 6 if yes then convert it yo complex datatype

# number = int(input("enter the number: "))
# if number%2==0 and number%6==0 :
#     complex_number = complex(number)
# print("yes")
# print(f"the number is divisible by 2 and 6 and converted to complex: {complex_number}")

#10  WAP to accept per from the user and display grade.
# per= int(input("enter your marks: "))
# if per>90:
#      print("A")
#      if per>80 and per<=90:
#          print("B")
#      if per>=60 and per<=80:
#           print("C")
#           if per<60:
#                print("D")




#  if else


#1   wap to check whether an year is leap year or not
# yr=int(input("enter the year: "))
# if yr%4==0:
#      print ("the enter year is leap year")
# else:
#      print("the entered year is not leap year")


#2 wap to check that the given string is pallindrome  or not
# str = 'madam'
# if str[::-1]==str:
#     print("palindrome")
# else :
#     print ("not palindrome")    


#3  wap to find the greatest of two numbers
# a = 5
# b = 6
# if  a<b:
#     print (f"{b} is greater")
# else :
#     print(f"{a} is greater")


#4 wap to check that the number is even or not if yes print even else make it even bt adding 1

# a = int(input("enter the number"))
# if a %2==0:
#     print("even")
# else:
#     print(a+1,": new number is even ")



#5  wap to check that the first character of the given string is uppercase or not if yes convert the whole string
#  into upper else capitalize it

# var = input("enter the character: ")
# if var[0].isupper():
#      print(var.upper())
# else:
#      print(var.capitalize())

#6  wap to check that the length of the string is even or not if yes reverse it else convert it into upper case
# n = "budd"
# if len(n)%2==0:
#     print (n[::-1])
# else:
#     print(n.upper())




#7  wap to check that the data is of individual data type or not

# var= 'asD'
# if isinstance( var,(int,float,complex,bool)):
#     print("individual datatype")
# ``

#8 wap to find that the given character is present in the given string or not
# str= (input("enter any string:  "))
# char = (input("enter any acharacter: "))

# if char in str:
#     print(f" the {char} character is present")
# else:
#     print (f" the {char} is not present")




#8   wap to print middle element of a tuple if its  of  string datatype and having even length

# tup = [10,20,40,50]

# if len(tup)%2 != 0:
#     mid = tup[len(tup)//2]
#     if type(mid) == str :
#         if len(mid)%2 == 0:
#             print(mid)
#         else :
#             print('not even length')
#     else:
#         print ("mid is not string type")
# else:
#     print("not have any mid value")




#9 wap to check that the number is greater than 5 or not if yes print as it is else make it negative.
# num = float(input("enter a number: "))
# if num>5:
#     print (f"the number is : {num} ")
# else:
#     print(f"The number is :{-num} ")




# if elif

#wap to print gretest number 

# a = int(input("enter any number: "))
# b= int(input("enter any number: "))
# c= int(input("enter any number: "))
# if a>b and a>c:
#     print(" a is greater number ")
# elif b<a and b>c:
#     print("b is grater number")
# else:
#     print("c is greater")


#wap to check that value is upper case or lowercase or digit and special character
# a= eval(input("enter any character: "))

# if a.isupper():
#     print ("character is upper case")
# elif a.lower():
#     print("character is lower case")
# elif a.isdigit():
#     print("character is digit")
# else:
#     print("character is special character")




# 1 wap to find the max element from list
# ls=[70,2,30,40]
# max=ls[0]

# for i in ls:
#     if i>max:
#         max = i
#         print("the maximum element is:", max)

#2 wAp to find second largest element from list



#9 wap to print the names which is starting with vowel in the given list
# names=["agra","banglore","mumbai","pune","indore"]
# i=0
# while i<len(names):
#     if names[i][0] in "aeiou":
#         print(names[i])
#     i+=1 


# str="Hello guys Good morning python is a programming language"
# char=input("enter a char:")
# i=0
# count=0
# while i<len(str):
#     if str[i]==char:
#         count+=1
#         print(f"the character {char} is present")
#     i+=1

