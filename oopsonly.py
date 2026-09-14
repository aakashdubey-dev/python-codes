#class and object in python
"""class student:
    name="spiderman"

s1=student()
print(s1.name)""" #this is how we create an class and object in python

#constructor concept
"""class student:
    def __init__(self,name):
        self.name=name
        print("constructor call")

s1=student("loki")
print(s1.name)

s2=student("hulk")
print(s2.name)"""

#class attribute and object attribute
"""class student:
    college_name="arya college of enginerring and IT" #class attribute

    def __init__(self,name,marks):
        self.name=name   #object attributes
        self.marks=marks

s1=student("arjun",95)
print(s1.name,s1.marks ,s1.college_name)"""

#questions 
"""class students:

    def __init__(self,name,marks1,marks2,marks3):
        self.name=name
        self.marks1=marks1
        self.marks2=marks2
        self.marks3=marks3


    def avg_marks(self):
        sum=self.marks1+self.marks2+self.marks3
        print("the avgscore is:",sum/3)

s1=students("ironman",90,99,90)
s1.avg_marks() """     

#static method 
"""class student:
    @staticmethod
    def hello():
        print("hello")

s1=student()
s1.hello()     #by instance
student.hello()# by class """

#encapsulation 
#question
"""class bank:
    acc_no=2341

    def __init__(self,amount,balance):
        self.amount=amount
        self.balance=balance

    def debit(self):
        curr_balance=self.balance-self.amount
        print(curr_balance)
                                           #wrapping the data and method 
    def credit(self):
        curr_balance=self.balance+self.amount
        print(curr_balance)


b=bank(700,10000)
b.debit()
b.credit()"""
