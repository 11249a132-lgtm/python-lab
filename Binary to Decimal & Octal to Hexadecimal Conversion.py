Aim:
To write a Python program that performs:
Binary to Decimal conversion, and
Octal to Hexadecimal conversion,
using functions.

Algorithm:
Start the program.
Define a function binary_to_decimal(binary_str)
Convert the binary string to a decimal integer using int(binary_str, 2).
Handle invalid input using exception handling (try-except).
Define another function octal_to_hexadecimal(octal_str)
Convert the octal number to decimal using int(octal_str, 8).
Convert decimal to hexadecimal using hex(decimal).
Remove the "0x" prefix and make it uppercase.
Handle invalid input using exception handling.
Display a menu with two choices:
(1) Binary to Decimal
(2) Octal to Hexadecimal
Accept user’s choice and input the corresponding number.
Call the appropriate function and display the result.
End the program.

Program (Python Code):
# Program: Binary to Decimal & Octal to Hexadecimal Conversion
# Function to convert Binary to Decimal
def binary_to_decimal(binary_str):
    try:
        decimal = int(binary_str, 2)
        return decimal
    except ValueError:
        return "Invalid Binary Number!"
# Function to convert Octal to Hexadecimal
def octal_to_hexadecimal(octal_str):
    try:
        decimal = int(octal_str, 8)  # Convert octal to decimal
        hexa = hex(decimal).upper().replace("0X", "")  # Convert to hexadecimal
        return hexa
    except ValueError:
        return "Invalid Octal Number!"
# Main program
print("=== Number System Conversion ===")
print("1. Binary to Decimal")
print("2. Octal to Hexadecimal")
choice = input("Enter your choice (1 or 2): ")
if choice == '1':
    binary = input("Enter a Binary Number: ")
    print("Decimal Value:", binary_to_decimal(binary))
elif choice == '2':
    octal = input("Enter an Octal Number: ")
    print("Hexadecimal Value:", octal_to_hexadecimal(octal))
else:
    print("Invalid choice! Please enter 1 or 2.")

Sample Output 1:
=== Number System Conversion ===
1. Binary to Decimal
2. Octal to Hexadecimal
Enter your choice (1 or 2): 1
Enter a Binary Number: 101101
Decimal Value: 45
Sample Output 2:
=== Number System Conversion ===
1. Binary to Decimal
2. Octal to Hexadecimal
Enter your choice (1 or 2): 2
Enter an Octal Number: 175
Hexadecimal Value: 7D
Sample Output 3 (Invalid Input):
=== Number System Conversion ===
1. Binary to Decimal
2. Octal to Hexadecimal
Enter your choice (1 or 2): 1
Enter a Binary Number: 1021
Decimal Value: Invalid Binary Number!

Result:

Thus, the Python program was successfully developed and executed to:
Convert a Binary number to Decimal, and
Convert an Octal number to Hexadecimal,
using functions with proper error handling for invalid inputs.
