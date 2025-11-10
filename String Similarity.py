Aim:
To write a Python program to find the similarity between two given strings and display it as a percentage.

Algorithm:
Start the program.
Input two strings from the user.
Use the SequenceMatcher class from the difflib module to compare the two strings.
Calculate the similarity ratio using ratio().
Convert the ratio into a percentage.
Display the similarity percentage.
End the program.

Program (Python Code):
# Program: String Similarity
from difflib import SequenceMatcher
# Step 1: Input two strings
str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")
# Step 2: Calculate similarity using SequenceMatcher
similarity_ratio = SequenceMatcher(None, str1, str2).ratio()
# Step 3: Convert to percentage
similarity_percentage = similarity_ratio * 100
# Step 4: Display the result
print(f"\nSimilarity between the strings: {similarity_percentage:.2f}%")

Result:
The Python program was successfully executed to calculate the similarity between two given strings, expressed as a percentage.
