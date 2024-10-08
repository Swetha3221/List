'''
'''
Write a Python Program to put the even and odd elements in a list into two different lists.

Input format:

Input consists of one integer and one list.

First input consists of the size of the list.

Second input consists of the elements based on the size.

Output format:

Output consists of two lists.

First list consists of all the even numbers in the list.

Second list consists of all the odd numbers in the list.

Sample Input:

5

1

2

3

6

5

Sample Output:

The even list [2, 6]

The odd list [1, 3, 5]

Ans:
# Input for the size of the list
n = int(input("Enter the size of the list: "))  # First input for the size of the list
my_list = []  # Initialize an empty list

# Collecting elements for the list
for _ in range(n):
    element = int(input())  # Input each element
    my_list.append(element)  # Add the element to the list

# Initialize lists for even and odd numbers
even_list = []
odd_list = []

# Separate even and odd numbers
for num in my_list:
    if num % 2 == 0:
        even_list.append(num)  # Add to even list
    else:
        odd_list.append(num)    # Add to odd list

# Output the lists
print("The even list", even_list)
print("The odd list", odd_list)
'''
'''
