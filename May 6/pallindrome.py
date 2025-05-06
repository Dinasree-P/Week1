def is_palindrome(s):
    # Convert the input string to lowercase for case-insensitive comparison
    s = s.lower()
    
    # Remove spaces from the string
    s = s.replace(" ", "")
    
    # Check if the string is equal to its reverse
    return s == s[::-1]

# Take input from the user
user_input = input("Enter a string to check if it's a palindrome: ")

# Call the function and print result
if is_palindrome(user_input):
    print("Yes, it's a palindrome.")
else:
    print("No, it's not a palindrome.")
