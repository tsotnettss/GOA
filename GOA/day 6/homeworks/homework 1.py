#Variable 1 number reference
num_1=float(input(" მონაცემი 1 დაბეჭდეთ ნებისმიერი რიცხვი 0 დან 15-ის ჩათვლით: "))
#Variable 2 number reference
num_2=float(input(" მონაცემი 2 დაბეჭდეთ ნებისმიერი რიცხვი 0 დან 15-ის ჩათვლით: "))
#Variable 3 number reference
num_3=float(input(" მონაცემი 3 დაბეჭდეთ ნებისმიერი რიცხვი 0 დან 15-ის ჩათვლით: "))
# x meaning
x=3
#The main computing operation
operation=((num_1+num_2+num_3)/x)
#Combinations corresponding to the operation
if operation > 9 and operation<10:
    print("გილოცავ მატრიცელო შენ გადმოგეცა 300 ლარიანი ბანძი ტოსტერი რასაც შეალიე შენი ცხოვრების წლები...")
elif operation <5:
    print("გილოცავ გაექეცი მატრიცას...")
elif operation >5 and operation < 9:
    print("YOU ARE MID")
elif operation <0 or operation >=10:
    print("there is something wrong with you")