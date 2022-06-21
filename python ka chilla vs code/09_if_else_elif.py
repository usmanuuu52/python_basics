age=input("please your age: ")
age=int(age)
if age>=5 and age<=10:
    print("welcome to school")
elif age>10 and age<15:
    print("you should join a college")
elif age>=15:
    print("you should join university")
else:
    print("Not eligible")