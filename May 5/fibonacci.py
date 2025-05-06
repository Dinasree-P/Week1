# Ask the user to input how many terms of the Fibonacci sequence to display
n = int(input("Enter the number of terms: "))

# Initialize the first two terms of the Fibonacci sequence
a, b = 0, 1

# Counter to keep track of how many terms have been printed
count = 0

# Loop until the desired number of terms is printed
while count < n:
    print(a)        # Print the current term
    a, b = b, a + b # Update values: a becomes b, b becomes a + b (next Fibonacci number)
    count += 1      # Increment the counter
