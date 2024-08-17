# Write code for algorithm 1 below
def count_down(n):
    # Base Case
    if n < 0:  # Handle both zero and negative cases
        return
    
    # Recursive Case
    print(n)
    count_down(n - 1)

# Test case
n = 8
count_down(n)

#another method for a countdown 
def count_down(n):
  #inherent base case
  #(will stop if n <= 0)
  if n>0:
      #recursive case
      print(n)
      count_down(n-1)
   
#test case
n=8
count_down(n)
