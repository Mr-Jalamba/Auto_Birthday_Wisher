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
   Doe,your_email@gmail.com,1998,12,11
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

Install the required modules:
```bash
pip install pandas
```

### Gmail Setup

1. Use a Gmail account for sending emails.
2. Enable **App Passwords** or **Allow Less Secure Apps** in Gmail settings.
3. Replace the `email` and `password` in the script with your Gmail credentials.

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
   email = "your_email@gmail.com"
   password = "your_app_password"
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
Email sent successfully
```

### Email
```
Subject: Happy Birthday!

Dear Doe,
Happy Birthday! Have an amazing day filled with joy and laughter.
```

---

## Error Handling

The script includes error handling for:
- **SMTP Connection Issues**: Handles connection timeouts or server errors.
- **Authentication Issues**: Handles invalid credentials.
- **General Errors**: Catches unexpected issues and logs them.

---

## Future Improvements

1. Support for multiple birthdays on the same day.
2. Enhanced error logging to track issues in a log file.
3. Add features to notify the sender about upcoming birthdays.
