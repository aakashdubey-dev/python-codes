"""a,b=10,20
print (a+b)

"""
#string
"""
a='aakash'
print(a)
print(a[:])
print(a[-4])
"""
#byte  (it is immutable)
#a=bytes([65,66,67,68])
#print(a)

#byte array  (it is mutable)
#b=bytearray([10,20,40])
#b[2]=65
#print(b)

#list  (it is mutable)
"""
a=[10,20,30.5,'aakash']
print(a)
a[1:3]=[6,7]
print (a)
a.append(15)
print(a)
"""
#tuple (it is immutable)
#a=(10,20,3.4,'aakash')
#print(a)

#range
#for i in range(1,10,2):
    #print(i)

#for i in range(10,0,-2):
    #print(i)

#set (it is mutable but indexing is not allowed)   
"""
a={10,20,'aakash'} 
print(a)
a.add(40)
print (a)
"""
#frozenset (its is immmutable )
#a=frozenset({10,3,'aakash'})
#print(a)

#dictonary (are in the pair of key and value)
#a={101:'aakash',102:'spiderman'}
#print(a)

#none (none mneans nothing)
#a=()
#print(a)

#wap to take the input from user and print their sum
"""
a=int(input("enter a:"))
b=int(input("enter b:"))
sum=a+b
print(sum)
"""
#wap tp print the area of rectangle
"""
length=int(input("enter a:"))
breadth=int(input("enter b:"))
area=length*breadth
print(area)
"""

#wap to use of ternary operator
"""
a=int(input("enter a:"))
b=int(input("enter b:"))
#print(True) if (a>=b) else print(False)
print(a>b)#without ternary"""

#code for count the length of the string 
#str1=input("enter the name :")
#print(len(str1))

#find the occurance 
#print(str1.count("a"))

#code for understanding the if elif else
"""
a=int(input("enter the number of student:"))

if(a==100):
    print("excellent score")
elif(a>=80 and a<=99):
    print("student achieve a grade")
elif(a>=60 and a<80):
    print("student achieve b grade")
else:
    print("pass only")"""

#program for odd even
"""a= int(input("enter the number: "))    

if(a%2==0):
    print("even number")
else:
    print("odd number")"""

#program for greatest of three number
"""a=int(input("enter the a:"))
b=int(input("enter the b:"))
c=int(input("enter the c:"))

if(a>b and a>c):
    print("a is greater")
elif(b>a and b>c):
    print("b is greater")
else :
    print(" c is greater") """       