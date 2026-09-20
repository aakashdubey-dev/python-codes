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
                                           #wrapping the data and method     def credit(self):
        curr_balance=self.balance+self.amount
        print(curr_balance)


b=bank(700,10000)
b.debit()
b.credit()"""

#del keyword in python
"""class car:
    model="maruti800"

    def __init__(self,price):
        self.price=price

    def priceandmodel(self):
        print(self.price,self.model)

c1=car(500000)
del c1.model    #to delete the specific attribute
del c1  # to delete the whole object
c2=car(600000)
c2.priceandmodel()
c1.priceandmodel()"""

#private concept in python
"""class employee:
    name="aakash"
    emp_id=2
    __salary=500000

    def __show(self):
        print(self.__salary,self.name)
                                            #method and attribute only access inside the class
    def display(self):
        self.__show()


e=employee()
# e.show()
# print(e.__salary)
e.display()"""

#inheritance 
#single inheritance
"""class car:
    @staticmethod
    def start():
        print("the car is started")

    @staticmethod
    def clutch():
        print("go for race")

class toyota(car):
    def __init__(self,name):
        self.name=name

        print(self.name)

c=toyota("fortuner")
c.start()"""

#multilevel inheritance
"""class car:
    @staticmethod
    def start():
        print("the car is started")

    @staticmethod
    def clutch():
        print("go for race")

class company(car):
    def __init__(self,brand):
        self.brand=brand

class model(company):
    def __init__(self,name,speed):
        self.name=name
        self.speed=speed
        n=company("toyota")

        print(self.name,self.speed,n.brand)


c=model("fortuner",120)
c.start()
"""

#multiple inheritance
"""class a:
    def display(self):
        print("i am a")

class b:
    def show(self):
        print("i am b")

class c(a,b):
    def watch(self):
        print("i am c")

c1=c()
c1.display()
c1.show()
c1.watch()"""

#super method
"""class car:
    def __init__(self,type):
        self.type=type
    @staticmethod
    def start():
        print("car stated")

class toyota(car):
    def __init__(self,name,type):
        super().__init__(type)
        self.name=name

        print(self.name,self.type)

c=toyota("fortuner","diesel")
c.start()"""

#class method 
"""class student:
    name="spiderman"
    # def details(self,name):
    #     self.__class__.name=name

    #to direct change the attribute in function
    @classmethod
    def details(cls,name):
        cls.name=name

st=student()
# st.details("aakash")
st.details("aakash")
print(st.name)
print(student.name)"""

#property decorator
"""class student:
    def marks(self,phy,chem,maths):
        self.phy=phy
        self.chem=chem
        self.maths=maths

    @property
    def percentage(self):
        return (self.phy+self.chem+self.maths)/3
        #percentage
    # def percentage(self):
    #     self.percentage=(self.phy+self.chem+self.maths)/3
    #     print(self.percentage)

st=student()
st.marks(90,90,90)
st.phy=54      #percentage will same
print(st.percentage)"""

#polymorphism
"""class complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img

    def show(self):
        print(self.real,"i+",self.img,"j")

    #normal function
    def add(num1,num2):
        newreal=num1.real+num2.real
        newimg=num1.img+num2.img
        num3=complex(newreal,newimg)
        return num3

    #dunder function
    # def __add__(num1,num2):
    #     newreal=num1.real+num2.real
    #     newimg=num1.img+num2.img
    #     num3=complex(newreal,newimg)
    #     return num3



num1=complex(1,2)
num1.show()

num2=complex(3,4)
num2.show()

num3=num2.add(num1)  # for my funtion
num3=num1+num2      #for dunder function because python automatically call it
num3.show()                
"""
#questions
"""class circle:
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return (3.14*self.radius*self.radius)

    def perimeter(self):
        return (2*3.14*self.radius)

c1=circle(21)
print(c1.area())
print(c1.perimeter())"""

"""class employee:
    def __init__(self,role,department,salary):
        self.role=role
        self.department=department
        self.salary=salary

    def showdetails(self):
        print(self.role,self.department,self.salary)

class engineer(employee):
    def __init__(self,name,age,role,salary,department):
        self.name=name
        self.age=age
        super().__init__(role,department,salary)

e1=engineer("Aakash",19,"manager",180000,"product")
e1.showdetails()"""

# class father:
#     hair_colour="black"

# class mother:
#     eye_colour="brown"

# class child(father, mother):

#     def displaygens(self):
#         print("hair-colour:",self.hair_colour,"|","eye-colour: ",self.eye_colour)

# c=child()
# c.displaygens()

# class shape:
#     def __init__(self,length,breadth,radius,shapee):
#         self.length=length
#         self.breadth=breadth
#         self.radius=radius
#         self.shapee=shapee

#     def area(self):
#             if(self.shapee=="rectangle"):
#                 return self.length*self.breadth
            
#             if(self.shapee=="circle"):
#                 return 3.14*self.radius*self.radius

# class rectangle(shape):
#      def __init__(self,length,breadth,shapee):
#         self.length=length
#         self.breadth=breadth  
#         self.shape=shapee
#         pass

# class circle(shape):
#      def __init__(self,radius,shapee):
#           self.radius=radius
#           self.shapee=shapee
#           pass

# c1=circle(1,"circle")
# print(c1.area())








