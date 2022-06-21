print("this is while loop")
x=0
while x<5:
    print(x)
    x=x+1
print("-----------------")

print("this is for loop")
for i in range(5,10):
    print(i)


for i in range(5,30,2):
    print(i)



days=["tuesday","monday","wednesday","friday"]
for i in days:
    print(i)


days=["tuesday","monday","wednesday","friday"]
for i in days:
    if i=="friday": #loops stops on reaching th friday and prints everythings before friday but not friday
        break
    print(i)


days=["tuesday","monday","wednesday","friday"]
for i in days:
    if i=="wednesday": #loops skips on reaching wednesday and prints ot evrything after taht but not wednesday
        continue
    print(i)



