# Problem 1: Filtering Even Numbers
"""
You have a list of integers. Write a Python function that uses filter and a lambda function 
to filter out the even numbers from the list.

Input Example:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Output Example:
[2, 4, 6, 8, 10]
"""

# Step 1: Define the list of numbers and print the original list.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Original list of numbers:", numbers)

# Solution 1: Using filter and lambda
# Step 2: Use filter with a lambda function to filter out even numbers.
evens = list(filter(lambda n: n % 2 == 0, numbers))

# Step 3: Print the filtered list of even numbers.
print("Filtered list (even numbers) using filter and lambda:", evens)

# Solution 2: Using list comprehension
# Step 4: Use list comprehension to achieve the same result.
evens2 = [num for num in numbers if num % 2 == 0]

# Step 5: Print the filtered list of even numbers (list comprehension).
print("Filtered list (even numbers) using list comprehension:", evens2)

# The expected output for both approaches should be [2, 4, 6, 8, 10].



# Problem 2: Squaring Numbers
"""
You have a list of integers. Write a Python function that uses map and a lambda function 
to return a new list where each element is the square of the original list.

Input Example:
numbers = [1, 2, 3, 4, 5]

Output Example:
[1, 4, 9, 16, 25]
"""

# Step 1: Define the list of numbers and print the original list.
numbers = [1, 2, 3, 4, 5]
print("Original list of numbers:", numbers)

# Solution 1: Using map and lambda
# Step 2: Use map with a lambda function to square each number.
squares = list(map(lambda n: n * n, numbers))

# Step 3: Print the list of squared numbers.
print("Squared numbers using map and lambda:", squares)

# Solution 2: Using list comprehension
# Step 4: Use list comprehension to square each number in the list.
squares2 = [num * num for num in numbers]

# Step 5: Print the list of squared numbers (list comprehension).
print("Squared numbers using list comprehension:", squares2)

# The expected output for both approaches should be [1, 4, 9, 16, 25].
