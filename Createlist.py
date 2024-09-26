'''
'''
Write a program to create a list and display it.

Input format:

Input consist of n+1 integers

First integer corresponds to the size of the list

Next n inputs corresponds to the elements in the list

Output format:

Output is an integer list

Sample Input

4

1

2

3

4

Output

1 2 3 4

Ans:
# Input
n = int(input("Enter the size of the list: "))  # First input for the size of the list
my_list = []  # Initialize an empty list

# Collecting elements for the list
for _ in range(n):
    element = int(input())  # Input each element
    my_list.append(element)  # Add the element to the list

# Output the list elements as space-separated values
print(*my_list)  # Using unpacking to print elements in the desired format
'''
'''
