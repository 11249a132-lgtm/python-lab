Aim:
To develop a Python program that searches a text file for:
Phone numbers in the format +919900889977.
Email addresses in the format sample@gmail.com.

Algorithm:
Start the program.
Import the re module for regular expressions.
Open the text file in read mode.
Read the content of the file.
Define regular expression patterns:
Phone numbers: \+91\d{10}
Emails: [a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}
Use re.findall() to search for all occurrences of phone numbers and email addresses.
Display the found phone numbers and emails.
Close the file.
End the program.

Program (Python Code):
# Program: Search Phone Numbers & Email Addresses in a File
import re
# Input the filename
filename = input("Enter the filename: ")
try:
    with open(filename, 'r') as file:
        content = file.read()
    # Pattern for phone numbers (+91XXXXXXXXXX)
    phone_pattern = r'\+91\d{10}'
    phones = re.findall(phone_pattern, content)
    # Pattern for email addresses
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    emails = re.findall(email_pattern, content)
    # Display the results
    print("\n=== PHONE NUMBERS FOUND ===")
    for phone in phones:
        print(phone)
    print("\n=== EMAIL ADDRESSES FOUND ===")
    for email in emails:
        print(email)
except FileNotFoundError:
    print("Error: File not found!")

Result:
The Python program successfully searches a text file for:
Phone numbers in the format +91XXXXXXXXXX, and
Email addresses like sample@gmail.com.
It lists all matches found in the file.
