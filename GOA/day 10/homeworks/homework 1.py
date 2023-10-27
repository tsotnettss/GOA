import random


simbol = ["~!@#$%^&*()_+=?><|':;}{'"]
alphabet = ["AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"]
num = ["0123456789"]

sim1 = random.choice(simbol[0])
sim2 = random.choice(simbol[0])

alp1 = random.choice(alphabet[0])
alp2 = random.choice(alphabet[0])

num1 = random.choice(num[0])
num2 = random.choice(num[0])
num3 = random.choice(num[0])
num4 = random.choice(num[0])

print("The new generated password is: ",sim1,sim2,alp1,alp2,num1,num2,num3,num4)