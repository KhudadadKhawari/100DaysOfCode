#If the bill was $150.00, split between 5 people, with 12% tip.
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Getting user input
print('_____tip Calculator_____')
bill = float(input('How much was the bill: '))
tip = int(input("how much tip you would give? (in percent):"))
people = int(input('how many people are paying for the bill?: '))

#Calculating the tip percentage and finding bill the total amount
tip_percentage = tip / 100
total_tip = bill*tip_percentage
bill_total = bill + total_tip

#Calculating bill per person and displaying the final output
bill_per_person = bill_total / people
final_amount = round(bill_per_person, 2)
print("Each Person should pay: ${:.2f}".format(final_amount))