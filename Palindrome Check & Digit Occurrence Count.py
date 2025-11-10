Aim:
To write a Python program to check whether a given number is a palindrome or not and to count the number of occurrences of each digit in the input number.
  
Algorithm:
Start the program.
Input a number from the user.
Store the number as a string for easy reversal and digit analysis.
Check if the string is the same when reversed.
If yes, display that the number is a palindrome.
Otherwise, display that it is not a palindrome.
Initialize an empty dictionary to store digit counts.
Iterate through each digit in the string:
Increment the count of that digit in the dictionary.
Display each digit and its occurrence count.
End the program.

Program (Python Code):
# Program: Palindrome Check & Digit Occurrence Count
# Step 1: Input a number from the user
num = input("Enter a number: ")
# Step 2: Check if the number is palindrome
if num == num[::-1]:
    print("\nThe number is a Palindrome.")
else:
    print("\nThe number is NOT a Palindrome.")
# Step 3: Count the occurrences of each digit
digit_count = {}
for digit in num:
    if digit in digit_count:
        digit_count[digit] += 1
    else:
        digit_count[digit] = 1
# Step 4: Display the digit occurrence count
print("\nDigit Occurrence Count:")
for digit, count in sorted(digit_count.items()):
    print(f"Digit {digit}: {count} time(s)")
  
Result:
Thus, the Python program was successfully executed to:
Check whether a given number is a palindrome or not, and
Count the number of occurrences of each digit in the input number.
