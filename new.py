## dictonary
"""info={"name":"aakash","age":20}
print(type(info))
print(info)"""

"""info={"name":"aakash","age":20,"subject":{"phys":98,"chem":87,"maths":96}}
info["rollno"]=2;
print(list(info["subject"]))
print(info["subject"]["chem"])"""

"""info={"name":"aakash","age":20,"subject":{"phys":98,"chem":87,"maths":96}}
dict_null={}
print(dict_null)
dict_null={"name":"aakash ji"}
"""

#normal functon  in dictonary
#info={"name":"aakash","age":20,"subject":{"phys":98,"chem":87,"maths":96}}
"""a=info.keys()
print(list(a))
print(len(info))  it als print the keys

b=info.values()
print(b)
print(list(b))"""

"""b=info.items()
print(b)       # return key value as tuple
pairs =list(info.items())
print(pairs[0])"""


"""r=info["name"]
d= info.get("name2")
f= info.get("name")
print(f)
print(d)
print(f)"""

# to adding the new dictonary in existing dictonary
"""info.update({"gender":"male"})
print(info)
print(list[info])"""

#set
#a={1,2,3,"aakash",3,4,5}

"""print(a)
print(type(a))
print(len(a))"""

"""a.add(("spiderman"))
a.add([1,2])    # error(coz list is mutuable)
print(a)"""

"""a.remove(9)  # keyerror
a.remove(2)
print(a)"""

"""a.clear()  # delete all the element from set
print(a)"""

"""a.pop()      # rendomly delete the elements from the string
a.pop()
a.pop()
print(a)
print(a.pop())"""

# union and intersaction function in set
set1={1,2,3,4}
set2={4,5,6,7,5}

"""a=set1.union(set2)  # giving the union od set
print(a)
print(set1)  #union doesn't change the existing set"""

"""a=set1.intersection(set2)  # return the common value
print(a)"""

#practice question for dict and set
"""a={"table":["onlywood art","precious thing"],"cat":"says meow"}
print(a)"""

#taking the input marks ans subject from user of diff subject and add in dict
"""x=input("enter subject1")
y=input("enter subject2")
a=int(input("enter phys marks"))
b=int(input("enter chem marks"))

marks={}
marks.update({x:a,y:b})
print(marks)"""

#find the methode to store 9 and 9.0 in set
"""a={9}
a.add("9.0")
print(a)
"""

#loop
# #print num from 1 to100
# a=1
# while (a<=100):
#     print("the numbers is",a)
#     a+=1

# print table 
# a=5
# i=1
# while(i<11):
#     print("5*",i,"=",a*i)
#     i+=1

# print(i)

#square of a number
# i=1
# while(i<11):
#     print("the square of",i,"is",i*i)
#     i+=1

#  a=[12,4,3,5,6,7,8,5,4,3,23]
#  i=0 
# target=int(input("enter the target:"))
# while(i<11):
#     if(a[i]==target):
#         print("index is:",i)
#         break
#     else:
#         i+=1

#print the element of the list
# a=[12,4,3,5,6,7,8,5,4,3,23]
# i=0

# while(i<11):
#     print(a[i],end=" ")
#     i+=1

#continue
# a=1
# while(a<11):
#     a+=1
#     if(a%2!=0):
#         continue
#     else:
#         print(a)

#for loop
# a=[1,2,3,4,5,6,7,8,9,0]
# target=int(input("enter the target"))
# for val in a:
#     print(val)

# for el in a:
#     if(el==target):
#         print("found")
#         break
#     elif(el!=target):
#         print("not found")
#         break

#range
# for i in range(7):
#     print(i)

#table
# a=20
# for i in range(11):
#     print(a,"*",i,"=",a*i)

#even number
# for i in range(2,12,2):
#     print(i)

#reverse slicing
# a=[1,2,3,4,5,6,7,8]
# for i in range(len(a)-1,-1,-1):
#     print(a[i])

#sum of numbers from 1 to 100
# sum=0
# for i in range(101):
#     sum+=i
#     i+=1
# print(sum)

#count digit
# num=int(input("enter the number:"))
# count=0
# while(num>0):
#     count+=1
#     num=num//10
# print(count)

#reverse the number
# num=int(input("enter the number:"))
# rev=0
# while(num>0):
#     rem=num%10
#     rev=rev*10+rem
#     num//=10

# print(rev)

#code for reverse triangle pattern
# n=5
# for i in range(n):
#     for j in range(n-i):
#         print("*",end="")
#     print()

# code for prime number
# n=18
# flag=1
# for i in range(2,10):
#     if(n%i==0 and i!=n):
#         flag=0
#         break

# if(flag==0):
#     print("not prime")
# else:
#     print("prime number")

#function in python

#simple code 
"""def calc_sum(a,b):
    return a+b
g=calc_sum(10,3)
print(g)
"""

#code for average marks 
"""def avgmarks(r,t,y):
    a=(r+t+y)/3
    return a

print(avgmarks(1,2,3))"""

#print length of list by function
# a=[1,2,3,5,6,7,8,7,4]
# print(len(a))

#wap to print the el of list
"""def printel(a):
    for item  in a:
        print(item,end=" ")

a={1,2,3,4,5}
printel(a)"""
#waf for factorial
"""def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact
n=4
print(factorial(n))"""

#function to print usd to inr
"""def conversion(amount):
    inr=amount*91
    print("the amount in usd to inr is:",inr)

amount=10
conversion(amount)"""

#default parameter
"""def defpara(b,a=6454):  #default parameteer are not on first position 
    c=a*b
    return c

print(defpara(6))"""

#recursion
"""def fact(n):
    if(n==1):
        return 1

    return n*fact(n-1)

print(fact(4))"""


#code for print the sum of n natural  number
"""def sum(n):
    if(n==1):
        return 1

    return n+sum(n-1)

n=5
print(sum(n))
"""

#code to print all the lement of list by recursion
"""def print_el(a,n):
    if(n==len(a)):
        return 

    print(a[n])
    return print_el(a,n+1)

list=[1,2,3,4,5]
print_el(list,0)"""

#code for fibonacci
# def fibonacci(n):
#     first=0
#     second=1
#     i=1
#     while(i<n):
#         fib=first+second 
#         first =second
#         second =fib
#         i+=1

#     return fib

# n=6
# print(fibonacci(n))

# def printn(n):
#     if(n==0):
#         print(n)
#         return

#     print(n)
#     printn(n-1)

# n=4
# printn(n)

#code to revise fibonacci in recursion
# def fibonacci(n):
#     if(n==0 or n==1):
#         return n

#     return fibonacci(n-1)+ fibonacci(n-2)

# n=4
# print(fibonacci(n))

#I/O operation on closed fil
#read operation
""""file=open("sample.txt","r")
data = file.read(6)
print(data)


d1=file.readline()
d2=file.readline()

print(d1)
print(d2)"""

# read operation
# file=open("demo.txt","a")  #we can alse create and write in the created file
"""file=open("demo.txt","a")   #append mode
file=open("demo.txt","w")   #write mode
data =file.write("\nhari kripa")

file.close()"""

# '+' opeartion 
# 'r+'
# file= open("sample.txt","r+")
# data = file.read()
# print(data)

# file.write("aakash ji  ")

#w+
# file=open("sample.txt","w+")
# file.write("akash")

# data=file.read()
# print(data)

#"a+"
# file=open("demo.txt","a+")

# data=file.read()
# print(data)


# file.write("\naakash is servant of god")

