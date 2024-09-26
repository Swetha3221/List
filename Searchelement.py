'''
'''
Write a Program to find the search element in the given list

Input & Output Format:

Input consists of one list and one integer.

First input consists of a size of a list.
Second inputs corresponds to the elements of list in single line separated by space.

Third input consists of the element which we need to search

Sample Input 1:

5

1 2 3 6 5

3

Sample Output 1:

3 is present in the given list

Sample Input 2:

5

1 2 3 6 5

4

Sample Output 2:

4 is not present in the given list
Ans:
# Input for the size of the list
n = int(input("Enter the size of the list: "))  # First input for the size of the list

# Input for the elements of the list in a single line separated by space
my_list = list(map(int, input("Enter the elements of the list: ").split()))  # Convert input to a list of integers

# Input for the element to search
search_element = int(input("Enter the element to search: "))  # The element to search for

# Check if the element is in the list
if search_element in my_list:
    print(f"{search_element} is present in the given list")
else:
    print(f"{search_element} is not present in the given list")
'''
'''
