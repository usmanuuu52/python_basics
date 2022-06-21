def age_future(age,text):
    age=age+20
    print("your age after 20 years would be: ",age,text)

age_future(20,"congrats")



def usman(details):
    print(details)

usman("i am usman from tangi charsadda")


def education(grade):
    grade=grade+2
    return grade

pr=education(5)
print(pr)



def names(first,last="nasir"): #this is parameters 
    print(f"Hi {first} {last} ")
names("usman")  #this is arguments



def multiply(*numbers):    # * is used to enter as many arguments as you want
    total=1
    for number in numbers:
        total=total*number
    print(total)

multiply(2,3,4,5,6,7)

def fizzbuzz(inp):
    if (inp%3==0) and (inp%5==0):
        return "fizzbuzz"
    if inp%3==0:
        return "fizz"
    if inp%5==0:
        return "buzz"
    
    return inp

print(fizzbuzz(60))


def conv(miles):
    km=1.6*miles
    print("your miles in km is :",km)

conv(3)