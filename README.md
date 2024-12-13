# Auto_Birthday_Wisher
Never forget to say happy birthday again!

Birthday Email Automation
This project automates the process of sending personalized birthday emails to recipients on their special day. It matches the current date with a list of birthdays from a CSV file, personalizes a pre-written letter template, and sends the email using Gmail's SMTP server.

How It Works
Checks the Current Date:

Compares today's month and day with the data in birthdays.csv.
Selects a Template:

Chooses a random birthday letter template from the letter_template folder.
Personalizes the Email:

Replaces the placeholder [NAME] in the template with the recipient's name.
Sends the Email:

Sends the email using Gmail's SMTP server.

Prerequisites:
Files
1. birthdays.csv: A CSV file with the following structure:

name,email,year,month,day
Doe,your_email@gmail.com,2000,12,25
name: Recipient’s name
email: Recipient’s email address
year, month, day: Recipient’s date of birth

2. Letter Templates: Text files stored in the letter_template folder. 
Example:

Dear [NAME],
Happy Birthday! Have an amazing day filled with joy and laughter.

Python Requirements
Python Version: 3.x
Modules Used:
pandas
smtplib
datetime
random
Install the required modules:

Gmail Setup
Use a Gmail account for sending emails.
Enable App Passwords or Allow Less Secure Apps in Gmail settings.
Replace the email and password in the script with your Gmail credentials.
Setup and Run
Folder Structure
Make sure your project is organized like this:

.
├── main.py                   # The Python script
├── birthdays.csv             # The CSV file with birthdays
└── letter_template/          # Folder containing letter templates
    ├── bday_letter1.txt
    ├── bday_letter2.txt
    ├── bday_letter3.txt
    
Steps
Set Your Email Credentials: Open main.py and set your Gmail address and app password:

email = "your_email@gmail.com"
password = "your_app_password"
Run the Script: Execute the script:

python main.py
Output:

If a match is found, the email is sent and a success message is displayed.
If no birthdays match today’s date, a message indicates no emails were sent.
Example Output

Email sent successfully

Email

Subject: Happy Birthday!

Dear Doe,
Happy Birthday! Have an amazing day filled with joy and laughter.

Error Handling
The script includes error handling for:

SMTP Connection Issues: Handles connection timeouts or server errors.
Authentication Issues: Handles invalid credentials.
General Errors: Catches unexpected issues and logs them.

Future Improvements
Support for multiple birthdays on the same day.
Enhanced error logging to track issues in a log file.
Add features to notify the sender about upcoming birthdays.
