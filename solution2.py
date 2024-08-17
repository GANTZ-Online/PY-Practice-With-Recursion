# Write code for algorithm 2 below

def natural_numbers(x, i=1):
    # Base Case: If i exceeds x, stop recursion
    if i > x:
        return
    
    # Print the current number followed by a space
    print(i, end=' ')
    
    # Recursive Case: Call the function with the next number
    natural_numbers(x, i + 1)

# Test case
natural_numbers(3)
