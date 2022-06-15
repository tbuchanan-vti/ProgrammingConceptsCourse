# Problem Definition
#####################
# Develop a program to find the amount of G.C.T. applicable and the total cost of a item (inclusive of tax).
# Assume the G.C.T. rate is 15 percent and the user will enter the cost of the item. 

# IPO
# Input - cost of the item 
# Process -
#   find the GCT applicable by multiplying the tax rate by the cost of the item  
#   find the sum of the GCT and the cost of the item to get the total cost 
# Output - total cost and GCT 

# data types - integer, float, string and character (surrounded by single quotes '7')
# cost = float(input("Enter the cost of the item:"))
# gct = cost * .15
# totalcost = cost + gct
# single plus sign (+) in programming has two meanings
# if two values are involved, plus means sum
# if two strings are involved, plus means concatenate/combine
# print("GCT applicable is $" + str(gct))
# print("Total cost of the item is $" + str(totalcost))

# balance = float (input("Enter Credit card balance"))
# annualinterest = (balance) / .18 
# print ("end of mount balance is $" + str(annualinterest))

balance = float(input("credit card balance at end of month:"))
interest = (balance) * 0.015
print("interest applicable is $" + str(interest))