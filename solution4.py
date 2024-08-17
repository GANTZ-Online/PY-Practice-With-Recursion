# Write code for algorithm 4 below
def power(a, b):
    # Base case
    if b == 0:
        return 1
    elif b == 1:
        return a
    else:
        # Recursive case
        return a * power(a, b - 1)

# Test cases
print(power(2, 4))  # Output: 16
print(power(3, 3))  # Output: 27