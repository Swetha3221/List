'''
'''
Write a Python Program to find the smallest number in a list

Input & Output Format:

Input consists of one list and one integer.

First input consists of a size of a list.

Second inputs corresponds to the size of the list.

Output consists of the largest element.

Sample Input:

5

1

2

3

6

5

Sample Output:

1
Ans:
# Input for the size of the list
n = int(input("Enter the size of the list: "))  # First input for the size of the list
my_list = []  # Initialize an empty list

# Collecting elements for the list
for _ in range(n):
    element = int(input())  # Input each element
    my_list.append(element)  # Add the element to the list

# Finding the smallest number in the list
smallest = my_list[0]  # Assume the first element is the smallest

for num in my_list:
    if num < smallest:
        smallest = num  # Update smallest if current number is smaller

# Output the smallest element
print(smallest)
'''
'''
