#implicit type conversion
x=10.3
y=34
z=x*y
print("The type is:",type(z))
a=input("please enter your name? ")
print("your name is:",a,"and age is",y)
x=str(x)
print("your name is: "+a+" and age is "+x)


#Explicit type conversion
x=10.2
x=str(x)
print(type(x))