import os
import smtplib
import socket
import datetime as dt
import pandas
import random

SENDER_EMAIL = ""
PASSWORD = ""
PLACEHOLDER = "[NAME]"
smtp_server = "smtp.gmail.com"
port = 587

birthday_data = pandas.read_csv("birthdays.csv")

# Use relative path to ensure correct location
file_path = os.path.join("letter_template", f"bday_letter{random.randint(1, 3)}.txt")
print(f"Looking for file: {file_path}")

today = dt.datetime.today()
current_month = today.month
current_day = today.day

matching_rows = birthday_data[(birthday_data["month"] == current_month) & (birthday_data["day"] == current_day)]
try:
    if matching_rows.empty:
        print("No matches for today's date.")
    else:
        matching_name = matching_rows.name.iloc[0]
        matching_email = matching_rows.email.iloc[0]

        # Open the file and replace placeholder
        with open(file_path, "r") as bday_letter:
            message = bday_letter.read()
            bday_message = message.replace(PLACEHOLDER, matching_name)

        # Send the email
        with smtplib.SMTP(smtp_server, port) as connection:
            connection.starttls()
            connection.login(user=SENDER_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=SENDER_EMAIL,
                to_addrs=matching_email,
                msg=f"Subject: Happy Birthday!\n\n{bday_message}"
                )
        print("Email sent successfully!")
except FileNotFoundError as e:
    print(f"File not found: {e}")
except (smtplib.SMTPConnectError, socket.timeout) as e:
    print(f"Failed to connect: {e}")
except smtplib.SMTPAuthenticationError as e:
    print(f"Authentication failed: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
