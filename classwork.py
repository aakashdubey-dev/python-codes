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

