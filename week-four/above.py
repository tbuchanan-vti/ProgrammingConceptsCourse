integer = int(input("enter integer:"))
if integer > 0 and integer <=2000:
    print("below")
else:
    if integer >2000:
        print("above")

annualsalary = float(input("enter salary:"))
if annualsalary >= 2000:
    print("Above")
else:
    if annualsalary < 2000:
        print("Below")

a = int(input("value of the first number: "))
b = int(input("value of the second number: "))
c = int(input("value of the third number: "))

#find and print average
sum = a + b + c
average = sum / 3
print ("The average is:", average)