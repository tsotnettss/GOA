#age of the user
age1=int(input("Enter your age...: "))
#Age of the user's father
age2=int(input("Enter your father's age...: "))
#The year from which we want to calculate the age
years=int(input())
for i in range(30):
    print("It will be your age ...: "+str(age1+i)+",  And your father's age will be...: "+str(age2+i)+".  "+"in "+ str(years+i) )