
import pandas
import datetime as dt
from random import randint, choice
from pathlib import Path
import smtplib
birthday_data = pandas.read_csv("birthdays.csv")
birthday_dict = birthday_data.to_dict(orient="records")

today = dt.datetime.today()
today_day = today.day


base_path = Path(".\\letter_templates\\")
files_in_base_path = base_path.iterdir()
letter_list = []
for item in files_in_base_path:
    if item.is_file():
        letter_list.append(item.name)

person_name_list = []
person_email_list = []
# my_smtp = #your emial provided SMTP details eg "smtp.gmail.com
# my_email = #your email address
# to_email = #receiver email address
# my_pass = #app password
#===finding today's date in the file===
for i in range(len(birthday_dict)):
    if birthday_dict[i]["day"] == today_day:
        person_name_list.append(birthday_dict[i]["name"])
        person_email_list.append(birthday_dict[i]["email"])
        chosen_letter = choice(letter_list)
        with open(f".\\letter_templates\\{chosen_letter}") as letter:
            content = letter.read()
            with open("sent.txt", mode="w") as sent_letter:
                updated_letter = content.replace("[NAME]", f"{birthday_dict[i]["name"]}")
                updated_letter = sent_letter.write(updated_letter)
            with smtplib.SMTP(my_smtp) as connect:
                connect.starttls()
                connect.login(user=my_email, password=my_pass)
                with open("sent.txt") as read_letter:
                    letter_content = read_letter.read()
                    connect.sendmail(from_addr=my_email, to_addrs=to_email, msg=f"Subject:Happy Birthday {birthday_dict[i]["name"]}\n\n{letter_content}")





