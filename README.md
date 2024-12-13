
# Birthday Email Automation

This project automates the process of sending personalized birthday emails to recipients on their special day. It matches the current date with a list of birthdays from a CSV file, personalizes a pre-written letter template, and sends the email using Gmail's SMTP server.

---

## How It Works

1. **Checks the Current Date**:
   - Compares today's month and day with the data in `birthdays.csv`.

2. **Selects a Template**:
   - Chooses a random birthday letter template from the `letter_template` folder.

3. **Personalizes the Email**:
   - Replaces the placeholder `[NAME]` in the template with the recipient's name.

4. **Sends the Email**:
   - Sends the email using Gmail's SMTP server.

---

## Prerequisites

### Files

1. **`birthdays.csv`**: A CSV file with the following structure:
   ```
   name,email,year,month,day
   Doe,your_email@gmail.com,2000,1,1
   ```

   - **name**: Recipient’s name
   - **email**: Recipient’s email address
   - **year, month, day**: Recipient’s date of birth

2. **Letter Templates**: Text files stored in the `letter_template` folder. Example:
   ```
   Dear [NAME],
   Happy Birthday! Have an amazing day filled with joy and laughter.
   ```

---

### Python Requirements

- **Python Version**: 3.x
- **Modules Used**:
  - `pandas`
  - `smtplib`
  - `datetime`
  - `random`
  - `os`

Install the required modules:
```bash
pip install pandas
```

### Gmail Setup

1. Use a Gmail account for sending emails.
2. Enable **App Passwords** or **Allow Less Secure Apps** in Gmail settings.
3. Replace the `SENDER_EMAIL` and `PASSWORD` in the script with your Gmail credentials.

---

## Setup and Run

### Folder Structure
Make sure your project is organized like this:
```
.
├── main.py                   # The Python script
├── birthdays.csv             # The CSV file with birthdays
└── letter_template/          # Folder containing letter templates
    ├── bday_letter1.txt
    ├── bday_letter2.txt
    ├── bday_letter3.txt
```

### Steps

1. **Set Your Email Credentials**:
   Open `main.py` and set your Gmail address and app password:
   ```python
   SENDER_EMAIL = "your_email@gmail.com"
   PASSWORD = "your_app_password"
   ```

2. **Run the Script**:
   Execute the script:
   ```bash
   python main.py
   ```

3. **Output**:
   - If a match is found, the email is sent and a success message is displayed.
   - If no birthdays match today’s date, a message indicates no emails were sent.

---

## Example Output

### Console
```
Email sent successfully!
```

### Email
```
Subject: Happy Birthday!

Dear Doe,
Happy Birthday! Have an amazing day filled with joy and laughter.
```

---

## Updated Code

```python
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

```

---

## Error Handling

The script includes error handling for:
- **SMTP Connection Issues**: Handles connection timeouts or server errors.
- **Authentication Issues**: Handles invalid credentials.
- **File Not Found**: Handles missing or misnamed template files.
- **General Errors**: Catches unexpected issues and logs them.

---

## Future Improvements

1. Support for multiple birthdays on the same day.
2. Enhanced error logging to track issues in a log file.
3. Add features to notify the sender about upcoming birthdays.
