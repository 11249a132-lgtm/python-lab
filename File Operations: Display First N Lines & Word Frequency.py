Aim:
To write a Python program that accepts a file name from the user and performs the following operations:
Display the first N lines of the file.
Find the frequency of a word provided by the user in the file.

Algorithm:
Start the program.
Input the file name from the user.
Open the file in read mode.
Input the value of N (number of lines to display).
Read the file line by line and display the first N lines.
Input a word from the user to search for its frequency.
Read the entire file content and count occurrences of the word using the count() method.
Display the word frequency.
Close the file.
End the program.
Program (Python Code):
# Program: File Operations - Display First N Lines & Word Frequency
# Input file name
filename = input("Enter the file name: ")
try:
    with open(filename, 'r') as file:
        lines = file.readlines()
    # Operation 1: Display first N lines
    N = int(input("Enter the number of lines to display: "))
    print(f"\n=== FIRST {N} LINES OF THE FILE ===")
    for i in range(min(N, len(lines))):
        print(lines[i], end='')
    # Operation 2: Frequency of a word
    word = input("\n\nEnter the word to find its frequency: ")
    # Join all lines into a single string
    content = ''.join(lines)
    frequency = content.lower().count(word.lower())  # case-insensitive count
    print(f"\nThe word '{word}' occurs {frequency} times in the file.")
except FileNotFoundError:
    print("Error: File not found!")

Result:
The program successfully performs the following file operations:
Displays the first N lines of the specified file.
Finds the frequency of a user-specified word in the file (case-insensitive).
