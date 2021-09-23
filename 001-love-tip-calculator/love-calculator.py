#Love Calculator
#Getting the input
name1 = input('What is Your Name: ')
name2 = input('What is their Name: ')

#Concatenating the names and changing to lower case
combined = (name1 + name2).lower()

#Calculating the letter count
t = combined.count('t')
r = combined.count('r')
u = combined.count('u')
e0 = combined.count('e')

l = combined.count('l')
o = combined.count('o')
v = combined.count('v')
e1 = combined.count('e')

#calculating the total count of letters
first_digit = t + r + u + e0
second_digit = l + o + v + e1

#putting the two digits together
score = int(str(first_digit)+str(second_digit))

#For Love Scores less than 10 or greater than 90, the message should be:
# "Your score is **x**, you go together like coke and mentos."
# For Love Scores between 40 and 50, the message should be:
# "Your score is **y**, you are alright together."
# Otherwise, the message will just be their score. e.g.:
# "Your score is **z**."
if (score < 10) or (score > 90):
  print(f"Your score is {score}, you go together like coke and mentos.")
elif (score >= 40) and (score <= 50):
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")