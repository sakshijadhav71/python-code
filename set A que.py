#1
# i=ord('A')
# while i<=ord('Z'):
#     print(chr(i), end=" ")
#     i+=1

#2
# i=ord('a')
# while i <= ord('z'):
#     print(chr(i), end=" ")
#     i+=1

#3
# i=ord('A')
# while i<=ord('Z'):
#     print(chr(i) ,chr(i+32), end=" ")
#     i+=1

#4
# num=20
# while num>=2:
#     print(num)
#     num-=2

#5
# s= "Hello guys good morning python is a programming language"
# count=0
# element='g'
# i=0
# while i<len(s):
#     if s[i]==element:
#         count+=1
#     i+=1

# print(f"the element {element} occures in collection {count} time ")

#6
# s="hello world"
# i=0
# while i<len(s):
#     print(s[i], end=" ")
#     i+=2

#7
# ls= ["vaidegi", "aishwini", "patil", "srindhi","sumita","rahul","priyanka","isha"]
# i=0
# length=len(ls)
# if length%2==0:
#     print("the lenhth of the name is even")
    

#8
# ls= (10,2,5,[10,20],"hello",True,(3,4,6),{2,7},{90:"upper"})
# i=0
# while i<len(ls):
#     element=ls[i]  
#     if type (element)  in (str,tuple,set,list,dict) :
#         print(element)
#     i+=1    

#9
# names=["agra","banglore","mumbai","pune","indore","isha"]
# i=0
# while i<len(names):
#     if names[i][0] in "aeiou":
#         print(names[i])
#     i+=1 

#10
# str="helloworld1234"
# i=0
# vowel="aeiou"
# digit="0123456789"
# result=""
# while  i<len(str):
#     char= str[i]
#     if char in vowel or char in digit:
#         result+=char
#     i+=1
# print(" Extracted elemnt in  vowels and digit", result)



#for loop

#1 wap to print number from 1-20 segregrate even and odd number into list
# even ,odd=[],[]
# for i in range(1,20):
#     if i%2==0:
#         even.append(i)
#     else:
#         odd.append(i)
# print("even list:\n",even,"\nodd list:\n",odd)        

#2 wap to print vowels and digit in a string
# str="hellopython123"
# vowels="aeiou"

# for i in str:
#     if i.isdigit():
#         print("digit",i)
#     elif i in vowels:
#         print("vowels",i)

#3 wap to capitalize only first letter of every word in the given list.
# ls=["sakshi","om","rahul","raha","usha","mira"]
# listt=[]

# for word in ls:
#     i=word.capitalize()
#     listt.append(i)
# print(listt)    

#4wap to extract only individual datatype from the given list.

# ls=["sakshi",[10,20,30],12,3.4,777,{10:34},(12,34,56),2+4j,True]
# i=[]
# for i in ls:
#     if type(i) in (int,float,complex,bool):
#         print(i, end=" ")

# 5 wap to extract only individual datatype from given list and sum of all the individual datatype.(not complete solution)
# ls=["sakshi",[10,20,30],12,3.4,777,{10:34},(12,34,56),2+4j,True]
# sum=0
# for i in ls:
#     if type(i)  in (int,float,complex,bool):
#         print(i)


#6 wap to print count of alphabets and numbers and space in the given string
# wap to check how many alphbets , digit or space present in string
# str='hsele123    '
# alpha,digit,space=0,0,0 
# for i in str:
#     if 'a'<=i<='z':
#         alpha+=1
#     elif '0'<=i<='9':
#         digit+=1
#     elif i ==' ':
#         space+=1
# print(alpha,digit,space)        


# 7 wap to chech how many words are present in the given sentence
# s="hello world sentence"
# count=0
# word=s.split()
# for i in word:
#     count+=1
# print("the total number of words in sentence:",count)


#8 wap to create a dictionary and print the characters  and its ascii value pair
# str="hello worls"
# asciidict={}

# for i in str:
#     asciidict[i]=ord(i)
# print("the character  of ascii value:",asciidict)

#9 wap to create a dictionary and traverse into it and if the length is even print as it is else reverse it

# names=["apple","banana","orange","lichi","google","microsoft"]
# dict={}

# for dict in names:
#     if len(dict)%2==0:
#         print(dict)
#     else:
#         print(dict[::-1])
# print(dict)        


#10 wap to print factorial of a number
# num=4
# fact=1
# for i in range (1,num+1):
#     fact*=i
#     print(fact)

#11 wap to create a dictionary with element and its count pair
# ls=["yellow","red","black","pink","orange","green","red","pink","yellow"]
# dict={}
# for i in ls:
#     if i in dict:
#         dict[i]+=1

#     else:
#         dict[i]=1
# print(dict)

#12  wap to find the length of the string without using inbuilt function
# str="Never Give Up"
# count=0
# for i in str:
#     count+=1
# print(count)                                                                                                                                                    

#13 wap to reverse a string without using inbuilt function
# str="you did it guys"
# rev=''
# for i in str:
#     rev=i+rev
# print(rev, end=" ")

#14 wap to print alternative char from given string
# str="hello world"
# for i in str:
#     print(str[::-1])
#     break

# 15 
# str="hellohai"
# newstr=''
# dict={}
# for i in str:
#     if i in dict:
#         dict[i]+=1
#     else:
#         dict[i]=1
# for i in str:
#     if dict[i]>1:
#         newstr+='-'        
#     else:
#         newstr+=i
# print(newstr)

#16
# s=("1","2","3","4")
# for i in s:
#    if ('-'.join(s)):
#       print(i, end="")

#17 wap to sum of numbers

# str='sony12India567pvt21ltd'
# sum=0
# for i in str:
#     if '0'<=i<='9':
#        sum+=int(i)
# print(f"the sum is:",sum)       

#19 wap to remove duplicates from the list without using inbuilt function

# d=[1,2,3,4,5,6,7,1,2,3,4]
# newls=[]
# for i in d:
#     if i not in newls:
#         newls.append(i)
# print(s)        

#20 wap  print all the missing numbers from 1-10 in the below list.(incomplete)

# l=[1,2,3,4,5,6,7,10,]
# for i in range(1,11):
#     print(i)


#21 wap to reverse a string
#(for loop)
# ls=[1,2,3,4]
# newls=[]
# for i in range(len(ls)-1,-1,-1):
#     newls.append(ls[i])
# print(newls)

#(while loop)
# ls=[1,2,3,4]
# i=0
# j=len(ls)-1
# while i<j:
#     ls[i],ls[j]=ls[j],ls[i]
#     i+=1
#     j-=1
# print(ls)   


#22 wap to  create a dictionary of word and reverse word in pair 
# sen="tommarow is weekend and nonveg special"
# dict={}
# split=sen.split()
# for i in split:
#     dict[i]=i[::-1]
# print(dict)    


#23 wap to create a dictionary index and word pair
# sen="how are you guys"
# print(dict(enumerate(sen.split())))

#24 wap to create a dictinary words and its length pair.
# sen="tommarow is weekend and nonveg special"
# dict={}
# split=sen.split()
# for i in split:
#     dict[i]=len(i)
# print(dict) 
# 

# 25 wap to create a dictionary character and its corresponding upper case characters
# str="sunday" 
# dict={}  

# for i in str:
#     dict[i]=i.upper()
# print(dict)    

#26 wap to create a dictionary ascii and chracter pair

# l=[89,51,111,77,108,120]
# dict={}
# for i in l:
#     dict[i]=chr(i)
# print(dict)

#27 wap to create a list of character and its ascii value pair
# str='sunday'
# asci=[]

# for i in str:
#     a=(i,ord(i))
#     asci.append(a)
# print(asci)    


#nested for loop
#28 wap to sum of same index element from list
# ls1=[1,2,3,4,5]
# ls2=[2,3,4,]
# ls3=[11,12,13,14,15]

# sumlist=[]

# # for i in range(len(ls1)):
# #     print( ls1[i]+ls2[i]+ls3[i])

# #using zip function
# for i, j ,k in zip(ls1,ls2,ls3):       
#     print(i+j+k)

#29 wap to pair values of both dictionary
# d= {"apple":45,"mango":67 ,"cherry":90,"berry":23}
# p={"kashmir":"ind","america":"usa","uk":"toronto","africa":"uganda"}
# print(dict(zip(d.values(),p.values())))

#30 wap to group fruit names and country pair only if fruit is even length.
# d= {"apple":45,"mango":67 ,"cherry":90,"berry":23}
# p={"kashmir":"ind","america":"usa","uk":"toronto","africa":"uganda"}
# for i, j in zip(d,p):
#     if len(i)%2==0:
#         print(i,j) 

#31 wap to print only the even character from each string in a list
# l=["programming","python","regular","class","bangalore"]
# for i in l:
#     print(i[::2])

#32  wap to extract and store the extensions of files in a list
# l=['forloop.txt','python.py','while.pdf','function.pptx','lambda.png','map.py','python.pdf','oops.py']
# lst=[]
# for i in l:
#     print(i.split('.')[1])

#33 wap to create a dictionary with words and its length pair which starts with vowels
# s="today is tuesday and attending python session"

# for i in s.split():
#     if i[0] in 'aeiou':
#         print(i,len(i))

#34  wap to create a dictionary with letter and its words starting with that letter pair
# s="hi hello good morning welcome to python session"
# dict={}
# for i in s.split():
#     if i[0] in dict:
#         dict[i[0]]+= [i]
#     else:
#         dict[i[0]] = [i]
# print(dict)     

#35 wap to create a dictionary of character and  its indices pair.

# s="hello python"
# dict={}

# for i,j in enumerate(s):
#     if j in dict:
#         dict[j]+=[i]
#     else:
#         dict[j]=[i] 
# print(dict)    
# # 

# 36 wap to using this list get the bellow output
# l= ('sun flower', 'lily flower','marigold flower','lion animal','tiger animal','eagle bird','snake animal','lotus flower', 'pigeon animal'  ) 
# dict={}
# for i,j  in l:
#     if j in dict:
#         dict[j]+=[i]
#     else:
#         dict[j]=[i]
# print(dict)
# 
# 
# 38 wap to check the given number is armstrong or not (armstrong= sum od cube of the digit)
# num=370


# # 40 
# s='hi how are you'

#wap to return the position of vowels in the given string
# str="helloworld"
# ls=[]
# vowels="aeiou"1

# for i in range(len(str)):
#     if str[i] in vowels:
#         ls.append(i)
# print(ls)        

#write a program to find length  of collection without using len function using for loop
# colle=[10,20,30,40]
# count=0
# for i in colle:
#     count+=1
# print(count)    

#write a profram to whether the entered username and password 
# is correct or not if not correct print enter again 
# username="sak@"
# password=123

# attempt=0
# maxattempt=1
# while attempt<maxattempt:
#     username = input("Enter username: ")
#     password = input("Enter password: ")
#     if username ==username and password==password:
#         print("correct")
#         break
#     else:
#         print("enter again")
#         attempt += 1  

# if attempt == maxattempt:
#     print("Maximum attempts reached. Access denied.")

# wap to extract all integer data items from tuple
# tup=(12,1.2,44,"sakshi",5+5j,[12,23,23,34],(1,2,3,3)) 

# # a=[]
# for i in tup:
#     if isinstance(i,int):
#        a.append(i)
# print(a)


#write a program to extract non default values from the list
# mixed_list = [0, 1, '', None, 2, 'hello', 3, False, 4, 'world', 5]

# nondefault=[]
# defaultvalues= {0, '',None,False}

# for i in mixed_list:
#     if i not in  defaultvalues:
#         nondefault.append(i)
# print(nondefault)


#write a program to check whether the length of element inside the list is 
# even or odd and i want the dictionary pair
# ls = ["apple", "banana", "kiwi", "pear", "grape"]

# dict={}
# for i in ls:
#     if len(i)%2==0:
#         dict[i]="even"
# else:
#     dict[i]='odd'
# print(dict)


#8
# s="hello guys tomorrow holiday"
# specified_char="d"

# for i in s:
#     if specified_char in i:
#         print(i)
#         break
#     else:
#         print(i)

#9
# l=[2,3,45,67,89,11,2,3,4,5,6,7,8,11]

# for i in l:
#     if i<10 or i>99:
#          continue
#     print(i)

# l=[1,5,-2,-45,-55,88,-100,-63]

# for i in l:
#     if i<0:
#         continue
#     print(i)


# str=input("Enter a string:")
# vowels=[]
# consonents=[]

# vowelset={'a','e','i','o','u','A','E','I','O','U'}

# for i in str:
#         if i in vowelset:
#             vowels.append(i)
#         else:
#             consonents.append(i)
# print(vowels,consonents)            
            
# user=(input("enter a homogeneous list of integer: "))
# numeber=[int(num) for num in user.split(",")]
# even=[]
# odd=[]
# i=0
# while i<len(numeber):
#     if  numeber[i]%2==0:
#         even.append(numeber[i])
# else:
#     odd.append(numeber[i])
#     i+=1

# print(f"even list:{even}")  
# print(f"odd list:{odd}")  


