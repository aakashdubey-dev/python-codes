#code for pattten making

#simple four coloumn pattern
"""n= int(input("enter the n:"))

for i in range(n):
    for j in range(n):
        print("*",end='')
    print()"""

#for triangle
"""n= int(input("enter the n:"))

for i in range(n):
    for j in range(i+1):
        print("*",end='')
    print()"""

#for reverse trangle
"""n= int(input("enter the n:"))

for i in range(n):
    for j in range(n-i):
        print("*",end='')
    print()"""

#trangle pattern but from right side
"""n= int(input("enter the n:"))

for i in range(n):
    for k in range(n-i-1):
        print(" ",end="")
    for j in range(i+1):
        print("*",end='')
    print()"""

#parallel line star pattern (verticaly)
"""n= int(input("enter the n:"))

for i in range(n):
    for j in range(n):
        if(j==0 or j==n-1):
            print("*",end="")
        else:
            print("  ",end='')   
    print()"""

#parallel line star pattern (horizontally)
"""n= int(input("enter the n:"))

for i in range(n):
    for j in range(n):
        if(i==0 or i==n-1):
            print("* ",end="")
        else:
            print("  ",end='')   
    print()"""

#code for hollow square
"""n= int(input("enter the n:"))

for i in range(n):
    for j in range(n):
        if(j==0 or j==n-1 or i==0 or i==n-1):
            print("* ",end="")
        else:
            print("  ",end='')   
    print()"""

#code to take the element from the user and save into a list
"""a=input("Enter the first character")
b=input("Enter third character")
c=input("Enter the second character")
list=[]
list.append(a)
list.append(b)
list.append(c)
print(list)"""

#code to check the listis palindrome or not
"""list=[1,2,1]
copy=list.copy()
copy.reverse()
if(copy==list):
    print("the string is palindrome")
else:
    print("the string is not palindrome")"""

#code to count the a grade student in tuple
"""grade=('a','b','a','c','d','a')
a=grade.count('b')
print(a)"""

#code for sort the list
"""grade=grade=['a','b','a','c','d','a']
a=grade.sort()
print(grade)"""

#code to convert the f and c  to k temperature function
# def fehranite_to_celcius(fehranite):
#     print("in celcius",(fehranite-32)*5/9)
# def celcius_to_fehranite(celcius):
#     print("in fehranite",(celcius+32)*9/5)
# def celcius_to_kelvin(celcius):
#     print("in kelvin: ",celcius+273.75)

# fehranite=98.6
# celcius=48
# fehranite_to_celcius(fehranite)
# celcius_to_fehranite(celcius)
# celcius_to_kelvin(celcius)


#code for factorial using return 
"""def fact(n):
    if(n==1):
        return n

    return n*fact(n-1)

print(fact(n=4))"""

#code for check even or odd using return
"""def check(n):
    if(n%2==0):
        return "even"
    if(n%2!=0):
        return "odd"

a=int(input("enter the number"))
print(check(a))"""
"""
#code for area of rectangle
def area(length,breadth):
    return length*breadth

a=int(input("enter the length"))
b=int(input("enter the breadth"))
print("the area is:",area(a,b))"""

#code for electricity bill
"""def bill(unit,n=6):
    return unit*n

unit=int(input("enter the units:"))
a=bill(unit) 
print(a)"""


# import pyttsx3
# import cowsay
# engine=pyttsx3.init()
# this =input("what is this ")
# cowsay.cow(this)
# engine.say(this)
# engine.runAndWait()

#code for random library
# import random
# otp=" "
# for i in range(6):
#     otp=otp+str(random.randint(0,9))
# print("your otp is",otp)





