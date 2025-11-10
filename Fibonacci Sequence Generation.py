Aim:
To write a Python program to generate the Fibonacci sequence up to N terms using a function. The program should display an error message if the input value of N is not greater than zero.

Algorithm:
Start the program.
Input a number N from the user (the number of terms in the Fibonacci sequence).
Check whether N is greater than 0.
If not, display an error message and terminate.
Define a function fibonacci(n) to generate and print the Fibonacci sequence up to n terms.
Initialize the first two terms: a = 0, b = 1.
Use a loop to generate the remaining terms as c = a + b.
Print the sequence.
End the program.

Program (Python Code):
# Program: Fibonacci Sequence Generation
def fibonacci(n):
    """Function to print the Fibonacci sequence up to n terms"""
    a, b = 0, 1
    print("\nFibonacci Sequence:")
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()  # for newline
# Step 1: Accept input from the user
try:
    n = int(input("Enter the number of terms (N > 0): "))

    # Step 2: Validate input
    if n <= 0:
        print("Error: Please enter a positive integer greater than 0.")
    else:
        fibonacci(n)
except ValueError:
    print("Error: Invalid input! Please enter an integer value.")

Sample Output 1:
Enter the number of terms (N > 0): 7
Fibonacci Sequence:
0 1 1 2 3 5 8
Sample Output 2:
Enter the number of terms (N > 0): 0
Error: Please enter a positive integer greater than 0.
Sample Output 3:
Enter the number of terms (N > 0): hello
Error: Invalid input! Please enter an integer value.

Result:
Thus, the Python program was successfully executed to generate the Fibonacci sequence up to N terms using a function and display an error message when the input does not satisfy the condition N > 0.
