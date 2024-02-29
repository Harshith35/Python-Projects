import random
import datetime as dt
import pandas as pd
import smtplib

MY_EMAIL = "mharshith305@gmail.com"
MY_PASSWORD = "fbsatbyykaljatej"

today = dt.datetime.now()
today_tuple = (today.month, today.day)

bdays = pd.read_csv("birthdays.csv")
for _ in range(len(bdays)):
    if bdays.iloc[_][3] == today_tuple[0] and bdays.iloc[_][4] == today_tuple[1]:
        file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
        with open(file_path) as letter_file:
            content = letter_file.read()
            content = content.replace("[NAME]",bdays.iloc[_][0])

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,to_addrs=bdays.iloc[_][1],
                                msg = f"Subject:Happy Birthday!\n\n{content}")
