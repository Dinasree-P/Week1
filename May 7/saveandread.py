def save_input(filename):
    # Ask the user for some text
    user_input = input("Enter some text: ")
    
    # Open (or create) the file and write their text
    with open(filename, "w", encoding="utf-8") as f:
        f.write(user_input)
    print("\nYour text has been saved!")  # Let them know it’s stored

def read_back(filename):
    # Try to open the file and show its contents
    try:
        with open(filename, "r", encoding="utf-8") as f:
            saved_text = f.read()
        print("\nReading what you wrote:")
        print(saved_text)  # Display the saved text
    except FileNotFoundError:
        # If the file isn’t there, tell the user
        print("\nNo file found to read from.")

if __name__ == "__main__":
    FILENAME = "user_input.txt"  # The name of our storage file
    
    # First, save the user’s input
    save_input(FILENAME)
    
    # Then ask if they want to see what was saved
    choice = input("\nDo you want to read the text? (y/n): ").strip().lower()
    if choice == "y":
        read_back(FILENAME)  # Only read if they say “yes”
    else:
        print("Okay")  # Exit