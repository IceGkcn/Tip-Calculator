#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? $"))
give_percent_tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people_count = int(input("How many people to split the bill?"))
tip = total_bill * give_percent_tip / 100
total_bill = total_bill + tip
payment = total_bill / people_count
per_payment = round(payment, 2) # I tried this but it is not working with 2 decimal like 44.00 it looks 44.0 this is not a rounding problem. this is a string formatting problem
# print(f"Each person should pay: {per_payment}$ ")
# So we can use below code for resolving this issue
print("Each person should pay: " + format(payment, '.2f'))
# or you can olso use  "{:.2f}".format(payment)
#print(format(33, '.2f'))
