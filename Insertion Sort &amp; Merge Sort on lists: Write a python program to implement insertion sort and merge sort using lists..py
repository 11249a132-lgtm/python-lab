Aim:
To write a Python program to implement Insertion Sort and Merge Sort on lists.

Algorithm:
Insertion Sort:
Start the program.
Input a list of numbers from the user.
Iterate from the second element to the end of the list.
Compare the current element with elements before it.
Shift elements to the right until the correct position is found.
Insert the current element in the correct position.
Repeat until the list is sorted.
Display the sorted list.
Merge Sort:
Start the program.
Input a list of numbers from the user.
Divide the list into two halves recursively until each sublist has one element.
Merge the sublists by comparing elements and creating a sorted list.
Repeat until the entire list is merged and sorted.
Display the sorted list.

Program (Python Code):
# Program: Insertion Sort & Merge Sort on Lists
# Insertion Sort function
def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    return lst
# Merge Sort functions
def merge_sort(lst):
    if len(lst) > 1:
        mid = len(lst) // 2
        left_half = lst[:mid]
        right_half = lst[mid:]
        merge_sort(left_half)
        merge_sort(right_half)
        i = j = k = 0
        # Merge left and right halves
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                lst[k] = left_half[i]
                i += 1
            else:
                lst[k] = right_half[j]
                j += 1
            k += 1
        # Copy remaining elements
        while i < len(left_half):
            lst[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            lst[k] = right_half[j]
            j += 1
            k += 1
    return lst
# Main Program
numbers = list(map(int, input("Enter numbers separated by space: ").split()))
print("\nOriginal List:", numbers)
# Insertion Sort
insertion_sorted = insertion_sort(numbers.copy())
print("List after Insertion Sort:", insertion_sorted)
# Merge Sort
merge_sorted = merge_sort(numbers.copy())
print("List after Merge Sort:", merge_sorted)

Result:
The Python program successfully implements Insertion Sort and Merge Sort on a list of numbers, displaying the sorted list for both sorting methods.
