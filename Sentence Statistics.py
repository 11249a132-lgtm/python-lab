Aim:
To write a Python program that accepts a sentence from the user and determines the number of words, digits, uppercase letters, and lowercase letters in the sentence.

Algorithm:
Start the program.
Accept a sentence from the user.
Initialize counters for:
Words
Digits
Uppercase letters
Lowercase letters
Split the sentence into words using split() to count the number of words.
Iterate through each character in the sentence:
If the character is a digit → increment digit_count.
If it is uppercase → increment upper_count.
If it is lowercase → increment lower_count.
Display all counts.
End the program.

Program (Python Code):
# Program: Sentence Statistics
# Step 1: Input a sentence from the user
sentence = input("Enter a sentence: ")
# Step 2: Initialize counters
word_count = len(sentence.split())
digit_count = 0
upper_count = 0
lower_count = 0
# Step 3: Iterate through each character
for ch in sentence:
    if ch.isdigit():
        digit_count += 1
    elif ch.isupper():
        upper_count += 1
    elif ch.islower():
        lower_count += 1
# Step 4: Display the results
print("\n=== SENTENCE STATISTICS ===")
print("Sentence:", sentence)
print("Number of Words:", word_count)
print("Number of Digits:", digit_count)
print("Number of Uppercase Letters:", upper_count)
print("Number of Lowercase Letters:", lower_count)

Result:
Thus, the Python program was successfully executed to count the number of words, digits, uppercase letters, and lowercase letters in a given sentence.
