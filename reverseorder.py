'''
'''
Write a program to print the given list in reverse order.

Sample Input:

10 20 30 40 50

Sample Output:

50 40 30 20 10
Ans:
# Input for the list elements
elements = input("Enter the list elements: ").split()  # Input list elements in a single line

# Reverse the list
reversed_list = elements[::-1]  # Slicing to reverse the list

# Output the reversed list
print(" ".join(reversed_list))  # Join the reversed list into a string and print
'''
'''
