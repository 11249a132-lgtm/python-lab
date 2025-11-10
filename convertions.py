def binary_to_decimal(binary_str):
    try:
        decimal = int(binary_str, 2)
        return decimal
    except ValueError:
        return "Invalid Binary Number!"


def octal_to_hexadecimal(octal_str):
    try:
        decimal = int(octal_str, 8)  # Convert octal to decimal (base 8)
        hexa = hex(decimal).upper().replace("0X", "")  # Convert decimal to hex
        return hexa
    except ValueError:
        return "Invalid Octal Number!"


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
