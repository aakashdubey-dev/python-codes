file=("student.txt","w")
name=input("enter name")
roll=(input("enter roll"))
classes=input("enter class:")

file.write("name="+name+"\n")
file.write("roll="+roll+"\n")
file.write("classes="+classes+"\n")

file.close()

file=open("student.txt","r")
print(file.read())
file.close()


file=open("spiderman.txt","w")
a=input("my name is aakash")

file.write("the output is:"+a)
file.close()

print(file.read())

file=("spiderman.txt","append")

b=file.append("my name is aakash ji")

print(file.read())
file.close()

