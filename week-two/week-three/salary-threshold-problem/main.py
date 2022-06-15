# Write a program that will determine whether you are 
# above the PAYE tax threshold of 1.5 million. The user
# should enter his/her annual salary. The program will print
# the text "above" if the salary is greater than 1.5 million
# and "below" if the salary is less than or equal to.

# Input - annual salary
# Process - compare salary entered against 1.5 million. if greater, print 
# "above". if less than or equal to, print "below"
# Output - string "above" or "below"

annual_salary = float(input("Enter annual salary: "))
if annual_salary > 1500000:
    print("above")
else:
    if annual_salary > 0 and annual_salary <= 1500000:
        print("below")
