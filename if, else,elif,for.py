# 1  WAP to check that the given programming language is present inside the given list

# lang= eval(input("enter a languages: "))
# lng=input("enter a language: ")
# if lang in lng :
#     print(lang)
#     print(f"{lang} is present")

# 2 WAP to check the number is even or odd
# a= int(input("enter any number"))
# if a %2==0:
#     print("even")
# else:
#     print("odd")

# 3 WAP to check the number is odd or not
# a = int (input("enter any number: "))
# if a%2!=0:
#     print(f"the number{a} is odd")

# 4 WAP to check the given no is divisible by 5
# a = int(input("enter any number: "))
# if a%5==0:
#     print(f"the number is {a} is divisible by 5 ")

# 5 WAP to check that the given no is positive.
# num = int(input("entyer any number: "))
# if num >0:
#     print(f"the number{num} is positive")

# 6  WAP to check the given string is pallindrome
# str = eval(input("enter any string: "))
# if str[::][-1]:
#     print ("the string is palindrome")

# 7 WAP to check that the first characcter of the given string is consonant.
# a = eval(input("enter the string: "))
# if a[0] not in "aeiou" :
#     print("The first character of string is consonant")

# 8 WAP to cheack that the given value is string
# a= input("enter a value: ")
# if isinstance(a, str):
#     print(f"The given value {a} is string")

# value=input('enter a string: ')
# if type(value) == str:
#     print(f"The given value {value} is a string")

# 9  WAP to check that the number is divisible by 2 and 6 if yes then convert it yo complex datatype
# 
# number = int(input("enter the number: "))
# if number%2==0 and number%6==0 :
#     complex_number = complex(number)
# print("yes")
# print(f"the number is divisible by 2 and 6 and converted to complex: {complex_number}")

#10  WAP to accept per from the user and display grade.

# per= int(input("enter your marks: "))
# if per>90:
#      print("A")
# elif per>80 and per<=90:
#          print("B")
# elif per>=60 and per<=80:
#           print("C")
# elif per<60:
#                print("D")



## if else ##

# 1 wap to check that the given string is palindrome or not palindrome.
# a= eval(input("enter a string: "))
# if a [::-1]==str:
#     print("The string is palindrome")
# else:
#     print("The string is not palindrome")

# 2 wap to check whether an year is leap year or not
# a= int(input("enter any year: "))
# if a%4==0:
#     print ("THE YEAR IS LEAP YEAR")
# else:
#     print("THE YEAR IS NOT LEAP YEAR")

# 3 wap to find greatest of two number
# a= 8
# b= 6
# if a>b:
#     print(f"{a} is greter")
# else:
#     print(f"{b} is greater")

# 4 wap to check that the number is even or not if yes print even else make it even bt adding 1.
# a= int(input("enter a number: "))
# if a%2==0:
#     print("even")
# else:
#     print(a+1,"new number is even")

#5  wap to check that the first character of the given string is uppercase or not if yes convert the whole string 
# into upper else capitalize it
# a= input("enter any value: ")
# if a[0].isupper:
#     print(a.upper())
# else:
#     print(a.capitalize())

#6  wap to check that the length of the string is even or not if yes reverse it else convert it into upper case
# a= 'heu'
# if len(a)%2==0:
#     print(a[::-1])
# else:
#     print(a.upper())


#7  wap to check that the data is of individual data type or not.
# var= 'sad'
# if isinstance( var,(int,float,complex,bool)):
#     print("individual datatype")
# else:
#     print("not individual datatype")

# 8 wap to find that the given character is present in the given string or not? 
# you have to take that string and character form user.
# str=input("enter any string: ")
# char=input("enter character: ")
# if char in str :
#     print (f"{char} char is present")
# else:
#     print (f"{char} is not present")

# 9 wap to check that the number is greater than 5 or not if yes print as it is else make it negative.
# num= 2
# if num >5:
#     print(num)
# else:
#     num=-abs(num)
#     print("the number is now negative", num)

# 10 wap to check that the given character is upper case, lower case, digit or a special character
# char= '@##'
# if char.isupper():
#     print("The character is uppercase",char)
# elif char.islower():
#     print ("the char is lower case", char)
# elif char.isdigit():
#     print("the char is digit", char)
# else:
#     print ("the charcter is special characger", char)

# 11 wap if the input is string return the length, if the list pop the element, 
# if tuple reverce it else print invalid value
# a= input("enter a value: ")
# if type(a)==str:
#     print(len(a))
# elif type(a)==list:
#     print(a.pop())
# elif type(a)==tuple:
#     print(a[::-1])
# else:
#     print("Invalid valiue")

# 12 wap to check the age 0-17 print child 18-3- print adult 31-60 print men 61 to 100 senior citizen.
# a= int(input("enter a age: "))
# if 0<= a<= 17:
#     print("child")
# elif 18<=a<=30:
#     print("adult")
# elif 31<=a<=60:
#     print("men")
# elif 61<=a <=100:
#     print("senior citizen")

# 13 wap to print smallest of three number
# a= int(input("enter a number: "))
# b= int(input("enter a number: "))
# c=int(input("enter a number:"))
# if a<b and a<c:
#     print("a is smallest")
# elif b<a and b<c:
#     print("b is smallest")
# else:
#     print("c is smallest")

# 14 wap to check the given number is even and divisible by 5
# a = int(input("enter any nuber: "))
# if a%2==0:
#     print("even")
# if a%5==0:
#     print ("divisible by 5")   


#15 wap to print middle element of a tuple if its  of  string datatype and having even length

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



#####4-10-24

# looping - If you want to perform some task or review set of instruction again and again when we use loop. 
# In python we have 2 loops 

# 1 while loop - In while loop we we don't know the exact number of iteration or how many time we have to perform 
#  task that time we use while loop. 
# In while loop we are going perform task based on some conditions if that condition is true then we are going to 
# execute the code reapetedly. 

# syntax
#  initialization 
# while condition:
#  SB
#  updation

# 1 wap print 1 to 10
# i = 1
# while i<=10:
#     print(i , end =' ')
#     i+=1


# 2 print a to z
# i = ord('a') 
# while i <= ord('z'):
#     print(chr(i), end =" ")
#     i+=1

# 3 print A to Z
# i = ord('A')
# while i <=ord ('Z'):
#     print(chr(i), end =" ")
#     i+=1



# 4 print AaBa
# i = ord('A')
# while i < ord('Z'):
#      print(chr(i), chr(i+32), end= " ")
#      i+=1


# 5 print 1 to 20 in reverse order
# i = 20
# while i>0:
#     print(i , end= " ")
#     i-=1



# 7  wap tp check for a perticular character is present in the given string or not.

# strr ='hello world'
# chrr = 'l'
# i =0
# while i < len(strr):
#     if  strr[i] == chrr:
#         print (f"the   character : {chrr} present at index : {i}")

#     i+=1    


# 8 wap  to fetch  perticular character of  index value.
# strr = "hello buddy"
# chrr = 'l'
# i=0
# cnt=0
# while i < len(strr):
#     if strr[i] == chrr:
#         cnt+=1

#     i+=1
# print(cnt)        


# 9 WAP  A to Z 
# i = ord('A')
# while i <ord('Z'):
#     print (chr(i), end=" ")
#     i+=1



# 10 wap to print 1-100 evan and odd numbers
# i = 1
# even, odd = [],[]
# while i <100:
#    if i%2==0:
#       even.append(i)
#    else:
#       odd.append(i)  
#    i+=1

# print ('odd list :\n' , even)
# print('\n\n')
# print ('even list :\n' , odd)

# 11 wap to check given string is palindrome or not
# strr='hello'
# i=0
# j=len(strr)-1
# while i < j:
#     if strr[i]!=strr[j]:
#         print('not pallindrome')
#         break
#     else:
#         print('pallindrome')
#     i+=1
#     j-=1

# 12 wap to print square of 10 integer
# num= 1
# while num<10:
#      print(num,num**2)
#      num+=1

# 13 wap to print like 10,20,30..300
# num = 10
# while num<=300:
#     print(num)
#     num= num+10

# 14 wap to print like 10,20,30..300
# num =105
# while num>7:
#     print (num)
#     num=num-7



# 15 print natural numners in reverce order.
# num =10
# while num>0:
#      print (num)
#      num= num-1

# num= 7
# sum= 0
# while num>1:
#     sum = sum+num
#     num-=1
# print (sum)




#8-10-24
# 16 wap to print given no in reverce order.
# num = 5346               # given number
# rev = 0                  #create  a variable 'rev'  and set it 0 to hold final reverce no
# while num>0:       
#     ld = num%10           #To get the last digit number
#     rev = rev*10+ld       
#   num = num//10      # remove the last digit from original number(floor division)
# print(rev)


# 17  wap to print sum of all digit of a number
# num = 123
# sum = 0

# while num>0:
#     ld = num%10
#     sum+=ld
#     num = num//10
# print(sum)


# 18 wap to check that the string is palindrome 
# str = 'sakshi'
# rev= ''
# i = len(str)-1
# while i >=0:
#     rev += str[i]
#     i-=1
# if rev == str:
#     print("palindrome")
# else:
#     print("not palindrome") 
      

# 19  wap to check that the last char is palindrome or not
# strr = 'aswe'
# i = 0
# j = len(strr)-1
# while i<j:
#    if strr[i] != strr[j]:
#     print('not palindrome')
#     break
#    else:
#      print('palindrome')
#      i+=1
#      j-=1
  
9-10-24
# for loop-  we know the exact no. iteration.
# range()- give us elements that we are store in range. it is a collection type.

# 1 print 1 to 20 alternate
# for i in range(1, 20, 2):
#     print(i , end = ' ')


# 2  print list of 1st letter
# i= ('hello','hi','how', 'soo', 'now')
# for i in i:
#     print (i[0])


# 3 print the table of a particular number taken from user using for loop
# a= int(input("enter a number: "))
# for i in range(1, 11):
#     print(a*i)

# 4 wap to access only the individual data from given list.
# ls = [10, 29, True, 3+7j, [10,300], 'hello', (67,667), 20.67 ]
# for i in ls:
#     if type(i) in [int,float,complex, bool]:
#         print(i)

#4 wap to find the mid value of a tuple if its a string of eeven lengthg 
# then only print it else print invalid

# tup = (30,20,'hello', 400,700)

# if len(tup)%2 !=0:
#     mid= len(tup)//2
#     if type (tup[mid]) ==str:
#         if len (tup[mid])%2==0:
#             print(tup[mid])
#         else:
#             print ('not even length')
#     else:
#         print('not a string')

# else:
#     print('not having a mis value')        


#5  wap to find that the specified character present in the given string or notch

# str= input ("enter a string: ")
# charr=input("enter a character: ")
# for i in range(len(str)):
#     if str[i] == charr:
#         print('presnt at index: ', i)


# #6 wap to fetch only the digit from given string using loop
# str = 'hello124'
# for i in str:
#     if '0' <=i <='9':
#         print(i, end=" ")


#7 wap to replace all the duplicate character from thr string with '-' without using any inbuilt function.
# strr = 'hello'
# dict = {}
# for i in strr:
#     if i in dict:
#         dict[i]+=1
#     else:
#         dict[i] =1

# newstr = ''
# for i in strr:
#     if dict[i] >1:
#         newstr +='-'
#     else:
#         newstr +=i
# print(dict)
# print(newstr)

#######################################


# 14-10-24

# alpha=''
# digit=''
# space=''
# str = 'Hellobuddy 12345q2'
# for i in str:
#     if 'a'<= i.lower()<='z':
#        alpha +=i
#     elif '0'<=i<='9':
#        digit+=i
#     else:
#        space +=''

# print(f'Alphabets : {alpha} \ndigits : {digit} \n space: {space}')


#Q1 you have a list of names and if the length of name is odd reverse it else store as its in the form of a dictionary
# lst = ['apple','banana','orange', 'mango']
# dict={}
# for i in lst:
#     if len(i)%2!= 0:
#         dict[i] = i[::-1]
#     else:
#         dict[i] = i

# print(dict)

# Q2 calculate how many words present in a given string.
# str='sakshi how are you'
# cnt=0
# for i in str.split():
#     cnt+=1
# print(f"total word :{cnt}")    


#join()-   its a inbuilt function which is used to join the perticular collection based on the spcified character
# and give me the final output in the form of string 
# join function is applied only on 'string' datatype
# syntax
# ''.join(col)

#WAP  ['1','2','3','4']   output : '1234'
# str= ['1','2','3','4']
# print(''.join(str))


### enumerate()-   enumarate function is used to bind the value of the collection with there index value and return
# your object addresss a containing all the tuples having index and value pair and to print the value from the 
# address you have to typecast
# lst= [10,20,30,40,50]
# print (tuple(enumerate(lst)))

# 3  [apple,banana apple ,apple] calculate how many time a word came in a list in the form of dictionary
# dictt= {}
# ls= ['apple', 'orange', 'banana', 'straberry', 'kiwi', 'litchi']

# for i in ls:
#     if len(i)%2 !=0:
#       dictt[i] = i[::-1]
#     else:
#        dictt[i] =i
# print(dictt)

# 15-10-24

# wap to  print name is present in list or not if yes print index value.
# ls= ['sakshi','siddhi','shreya']
# name= input("enter a name: ")
# for i in range(len(ls)):
#     if ls[i] ==name:
#         print(f"present at index :{i}")
#         break
    
#zip() - return object  
# ex
# ls1=[10,20,30]
# ls2=[100,200,300]
# print(list(zip(ls1,ls2)))
# for i, j in zip(ls1 ,ls2):
#     print(i,j)      


# ls1=[10,20,30]
# ls2=[100,200,300]
# print(list(zip(ls1,ls2)))
# for i, j in zip(ls1, ls2):
#     print(i+j)    #  if u want to add the  list


#19-10-2024
# transfer control statements

#1 break- breck the condition whatever we are mention in loop.
#ex
# for i in range(1,11):
#     if i==5:
#         break
#     print(i)
#2 continue- To skip the current iteration, moov on to the next.
# for i in range(1,11):
#     if i==5:
#         continue
#     print(i)
#3 pass- when we dont know what to pass in the condition we use pass statements.
# for i in range  (1,11):
#     if i==5:
#         pass
#     else:
#         print(i)


#palindrome or not without slicing
# s='madam'

# j=len(s)-1
# for i in range(len(s)//2):
#     if s[i]!=s[j]:
#         print("not pali")
#         break
#     j-=1
# else:
#         print("pali")
                                                                       
# s="sakshi"
# s=chr(ord(s[0])-32) + s [:1]
# print(s)



#wap to check no is strong no or not

# num=132
# sum=0
# for i in str(num):
#     fact=1
#     for j in range(1, int(i) +1):
#       fact *=j
#     sum+=fact


# if sum==num:
#    print("it's a strong no")
# else:
#    print("its not strong no")
    