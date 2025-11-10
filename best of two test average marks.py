Aim:
To write a Python program to find the best of two test average marks out of three test marks entered by the user.

Algorithm:
Start the program.
Input three test marks from the user.
Store the marks in a list.
Sort the list in descending order (highest marks first).
Select the first two elements from the sorted list (best two marks).
Calculate the average of these two best marks.
Display all three test marks, the two best marks, and the average of the best two.
End the program.

program:
# Program: Best of Two Test Average
# Step 1: Input three test marks
test1 = float(input("Enter marks for Test 1: "))
test2 = float(input("Enter marks for Test 2: "))
test3 = float(input("Enter marks for Test 3: "))
# Step 2: Store marks in a list
marks = [test1, test2, test3]
# Step 3: Sort marks in descending order
marks.sort(reverse=True)
# Step 4: Take the best two marks
best_two = marks[:2]
# Step 5: Calculate the average of the best two
average = sum(best_two) / 2
# Step 6: Display the results
print("\n=== RESULT ===")
print("Test Marks:", marks)
print("Best Two Marks:", best_two)
print("Best of Two Test Average:", round(average, 2))

output:
Enter marks for Test 1: 67
Enter marks for Test 2: 89
Enter marks for Test 3: 76
=== RESULT ===
Test Marks: [89.0, 76.0, 67.0]
Best Two Marks: [89.0, 76.0]
Best of Two Test Average: 82.5

Result:
Thus, the Python program was successfully executed to calculate the best of two test average marks out of three test marks entered by the user.
