##################### Extra Hard Starting Project ######################
import datetime as dt
import pandas
import random
import smtplib
import os


my_email = "randommail@gmail.com"
password = "secretpassword"

# 1. Update the birthdays.csv
# done manually

# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
todays_month = now.month
todays_date = now.day

bday_csv = pandas.read_csv("birthdays.csv")
bdays = bday_csv.to_dict(orient="records")

for dictionary in bdays:
    if dictionary["month"] == todays_month and dictionary["day"] == todays_date:

        # choosing a random letter
        random_letter = random.choice(os.listdir("letter_templates"))
        print(random_letter)

        # reading the chosen letter
        with open(f"letter_templates/{random_letter}", 'r') as file:
            filedata = file.read()

        # replacing the target string and writing it to a new file
        with open(f"to_send/{dictionary['name']}_bday_letter", 'w') as file:
            filedata = filedata.replace('[NAME]', dictionary["name"])
            file.write(filedata)
        with open(f"to_send/{dictionary['name']}_bday_letter", 'r') as file:
            message = file.read()

        # 4. Send the letter generated in step 3 to that person's email address.

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=dictionary["email"],
                msg=f"Subject:Happy Birthday!\n\n{message}."
            )



