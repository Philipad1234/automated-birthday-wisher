import datetime as dt
import pandas
import random
import smtplib
from details import *

PLACEHOLDER = '[NAME]'

now = dt.datetime.now()
today_month = now.month
today_day = now.day

data = pandas.read_csv('birthdays.csv')
birthdays = data.to_dict(orient='records')
letter_number = random.randint(1, 3)

for item in birthdays:
    if item['month'] == today_month and item['day'] == today_day:
        name = item['name']
        birthday_person_email = item['email']
        with open(f'letter_templates/letter_{letter_number}.txt') as letter_file:
            letter_content = letter_file.read()
            new_letter = letter_content.replace(PLACEHOLDER, name)
        with smtplib.SMTP(SMTP_SERVER, PORT) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(MY_EMAIL, birthday_person_email, msg=f'Subject:Happy Birthday\n\n{new_letter}')






