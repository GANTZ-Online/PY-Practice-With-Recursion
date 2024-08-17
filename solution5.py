# Write code for algorithm 5 below
def is_palindrome(s):
    # Base case: if the string is empty or has one character
    if len(s) <= 1:
        return True
    
    # Recursive case: compare first and last characters
    if s[0] == s[-1]:
        return is_palindrome(s[1:-1])
    else:
        return False

# Test cases
print(is_palindrome("madam"))   # Output: True
print(is_palindrome("radar"))   # Output: True
print(is_palindrome("hello"))   # Output: False