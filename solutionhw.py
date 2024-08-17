# Write a Python function called max_num() to find the max of three numbers.

def max_num(a, b, c):
    # Use the built-in max() function to find the maximum value among the three inputs
    return max([a, b, c])

# Test the max_num function with various inputs
print(max_num(1, 2, 3))  # Output: 3
print(max_num(100, 50, 1))  # Output: 100
print(max_num(15, 30, 2))  # Output: 30

# Write a Python function called mult_list() to multiply all the numbers in a list.

def mult_list(lst):
    # Check if the list is empty
    if len(lst) == 0:
        # Return 0 if the list is empty
        return 0
    
    # Initialize the product with the first element of the list
    prod = lst[0]

    # If there are more elements in the list, multiply them together
    if len(lst) > 1:
        for i in lst[1:]:
            prod *= i  # Update the product with each element
    
    # Return the final product
    return prod
    
# Test the mult_list function with various inputs
print(mult_list([1, 2, 3]))  # Output: 6
print(mult_list([]))  # Output: 0 (special case for empty list)
print(mult_list([15]))  # Output: 15 (only one element in the list)

# Write a Python function called rev_string() to reverse a string.

def rev_string(my_str):
    # Use slicing to reverse the string
    return my_str[::-1]

# Test the rev_string function with various inputs
print(rev_string(""))  # Output: "" (empty string)
print(rev_string("apple"))  # Output: "elppa"
print(rev_string("mt string"))  # Output: "gnirts tm"

# Write a Python function called num_within() to check whether a number falls in a given range.

def num_within(x, a, b):
    # Check if x is within the range [a, b] inclusive
    return x in range(a, b + 1)
     
# Test the num_within function with various inputs
print(num_within(3, 2, 4))  # Output: True (3 is between 2 and 4 inclusive)
print(num_within(3, 1, 3))  # Output: True (3 is between 1 and 3 inclusive)
print(num_within(10, 2, 5))  # Output: False (10 is not between 2 and 5 inclusive)

# Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.

# Initial rows of Pascal's triangle
triangle = [[1], [1, 1]]

def pascal(n):
    # Handle the case where the number of rows is less than 1
    if n < 1:
        print("invalid number of rows")
    elif n == 1:
        print(triangle[0])  # Print only the first row
    else:
        row_number = 2  # Start from the third row
        # Generate rows until we have n rows
        while len(triangle) < n:
            row = []  # Create a new row
            row_prev = triangle[row_number - 1]  # Get the previous row
            length = len(row_prev) + 1  # New row will have one more element
            
            for i in range(length):
                if i == 0:
                    row.append(1)  # The first number in the row is always 1
                elif i > 0 and i < length - 1:
                    # Intermediate numbers are the sum of two numbers from the previous row
                    row.append(triangle[row_number - 1][i - 1] + triangle[row_number - 1][i])
                else:
                    row.append(1)  # The last number in the row is always 1
            
            triangle.append(row)  # Add the new row to the triangle
            row_number += 1  # Move to the next row
        
        # Print each row of the triangle
        for row in triangle:
            print(row)

# Test the pascal function with various numbers of rows
pascal(2)  # Prints the first 2 rows of Pascal's triangle
pascal(5)  # Prints the first 5 rows of Pascal's triangle
