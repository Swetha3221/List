'''
'''
Write a program to count the number of times the given value is repeated.

Input Format:

First line of input consists of our list elements.

Second line of input consists of value to count.

Output Format:

Print thr number of times the given value is repeated in the list.

Sample Input:

10 20 10 40 10

10

Sample Output:

3
Ans:
# Input for the list elements
elements = input("Enter the list elements: ").split()  # Input list elements in a single line
my_list = list(map(int, elements))  # Convert input to a list of integers

# Input for the value to count
value_to_count = int(input("Enter the value to count: "))  # The value to count in the list

# Count the occurrences of the given value
count = my_list.count(value_to_count)

# Output the count
print(count)
'''
'''
