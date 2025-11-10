Aim:
To write a Python program that checks whether a phone number matches the pattern 415-555-4242:
Without using regular expressions (using a function isphonenumber()).
Using regular expressions.

Algorithm:
Without Regular Expression:
Start the program.
Input a phone number from the user.
Check the length of the input (should be 12).
Check that the 4th and 8th characters are '-'.
Check that all other characters are digits.
Return True if all conditions are met, otherwise False.
With Regular Expression:
Import the re module.
Define a pattern for the phone number: \d{3}-\d{3}-\d{4}.
Use re.fullmatch() to check if the input matches the pattern.
Return True if it matches, otherwise False.

Program (Python Code):
# Program: Check Phone Number Pattern
# Function to check phone number without regular expression
def isphonenumber(number):
    if len(number) != 12:
        return False
    if number[3] != '-' or number[7] != '-':
        return False
    for i, ch in enumerate(number):
        if i in [3, 7]:
            continue
        if not ch.isdigit():
            return False
    return True
# Function to check phone number using regular expression
import re
def isphonenumber_regex(number):
    pattern = r'\d{3}-\d{3}-\d{4}'
    return bool(re.fullmatch(pattern, number))
# Main Program
phone = input("Enter a phone number (format: 415-555-4242): ")
# Using non-regex function
if isphonenumber(phone):
    print("Valid phone number (without regex).")
else:
    print("Invalid phone number (without regex).")
# Using regex function
if isphonenumber_regex(phone):
    print("Valid phone number (with regex).")
else:
    print("Invalid phone number (with regex).")

Result:
The program successfully checks whether a phone number matches the pattern XXX-XXX-XXXX using:
A custom function without regular expressions, and
A function using regular expressions.
Both methods validate the phone number accurately.
