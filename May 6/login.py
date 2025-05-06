def register():
    # Ask the user to set a username and password
    print("=== Registration ===")
    username = input("Set your username: ")
    password = input("Set your password: ")
    return username, password

def login(saved_username, saved_password):
    # Ask the user to log in with the previously set credentials
    print("\n=== Login ===")
    entered_username = input("Enter your username: ")
    entered_password = input("Enter your password: ")

    # Check if entered credentials match the saved ones
    if entered_username == saved_username and entered_password == saved_password:
        print("Login successful!")
    else:
        print("Invalid username or password.")

# Run the registration first
user, pwd = register()

# Then ask for login
login(user, pwd)
