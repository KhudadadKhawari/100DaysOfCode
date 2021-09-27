import datetime
import pandas
import random
import smtplib

EMAIL = 'YOUR E-MAIL ADDRESS HERE'
PASSWORD = 'YourEmailPasswordHere'

# update if you added more leteters to the letter_templates directory
LETTERS = ['letter_templates/letter_1.txt','letter_templates/letter_2.txt','letter_templates/letter_3.txt'] 


# 1. Update the birthdays.csv
# 2. Check if today matches a birthday in the birthdays.csv

df = pandas.read_csv('birthdays.csv')
birthdays_list = df.to_dict(orient='records')


current_date = datetime.datetime.now()
current_day = current_date.day
current_month = current_date.month


people_born_on_current_date = []
for person in birthdays_list:
    if person['month'] == current_month and person['day'] == current_day:
        people_born_on_current_date.append(person)



# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
if people_born_on_current_date:
    for person in people_born_on_current_date:
        try:
            with open(random.choice(LETTERS), 'r') as file:
                current_letter = file.read().replace('[NAME]',person['name'])
        except FileNotFoundError:
            print('The Letter not Found, Please Check the letters list for the coorect files paths') # comment this line before deployment
            #pass ## un comment this line before deployment
        # 4. Send the letter generated in step 3 to that person's email address.
        else:
            reciever = person['email'].strip()
            subject = "Happy Birthday"
            with smtplib.SMTP('smtp.gmail.com',587) as session:
                session.starttls()
                session.login(EMAIL,PASSWORD)
                session.sendmail(from_addr=EMAIL,to_addrs=reciever,msg=f"Subject:{subject}\n\n{current_letter}")

                # print(f'EMAIL:{EMAIL} \nReciever:{reciever} \nSubject:{subject} \nEmail:{current_letter}')
