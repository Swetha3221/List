'''
'''
Write a program to find the sum of the elements in the array.

Input Format:

Input consists of n+1 integers where n corresponds to the number of elements in the array.

The first integer corresponds to n and the next n integers correspond to the elements in the array.

Assume that the maximum number of elements in the array is 20.

Output Format:

Output consists of a double value which corresponds to the mean of the array.

Refer sample input and output for formatting specifications.

Sample Input:

5

2

4

1

3

1

Sample Output:
11
Ans:
# Input for the size of the array
n = int(input("Enter the number of elements in the array: "))  # First input for the size of the array
my_array = []  # Initialize an empty array

# Collecting elements for the array
for _ in range(n):
    element = int(input())  # Input each element
    my_array.append(element)  # Add the element to the array

# Calculate the sum of the elements
total_sum = sum(my_array)

# Output the sum
print(total_sum)
'''
'''
