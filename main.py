##################### Extra Hard Starting Project ######################
import datetime as dt
import random
from pandas import *
import smtplib
# 1. Update the birthdays.csv
data = pandas.read_csv("birthdays.csv").to_dict(orient="records")
print(data)

# month_birth = data["month"]
# month_day = data["day"]
# email_name = data["email"]
# name_person = data["name"]
# print(email_name,month_day)
now = dt.datetime.now()
month = now.month
day = now.day
random_number = random.randint(1, 3)

My_email = "dnurmamatoff@gmail.com"
my_password = "akmal69!@#"

for person in data:
    if person["month"] == month and day == person["day"]:
        with open(f"./letter_templates/letter_{random_number}.txt", "r") as main_file:
            one_file = main_file.read()
            new_letter = one_file.replace("[NAME]", person["name"])
        print(new_letter)
        # with open(f"{name_person}.txt", "w") as my_file:
        #     my_file.write(new_letter)
        #
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(My_email, my_password)
            connection.sendmail(from_addr=My_email, to_addrs=person["email"], msg=f"Subject: Happy Birthday my {person['name']}\n\n"
                                                                             f"{new_letter}")

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




