# Write code for algorithm 3 below
def fibonacci(n):
    # Base cases
    if n <= 1:
        return n
    elif n == 1:
        return 1
    else:
        # Recursive case
        return fibonacci(n - 1) + fibonacci(n - 2)

n=14

# Test cases
print(fibonacci(4))  # Output: 3
print(fibonacci(2))  # Output: 1
