def temperature_converter():
    # Ask user for conversion direction
    choice = input("Convert to (C)elsius or (F)ahrenheit? ").strip().upper()

    # Take temperature input from user
    temp = float(input("Enter temperature: "))

    if choice == 'C':
        # Convert Fahrenheit to Celsius
        result = (temp - 32) * 5/9
        print(f"{temp}°F is {result:.2f}°C")
    elif choice == 'F':
        # Convert Celsius to Fahrenheit
        result = (temp * 9/5) + 32
        print(f"{temp}°C is {result:.2f}°F")
    else:
        # Handle invalid conversion choice
        print("Invalid choice. Please enter 'C' or 'F'.")

# Example usage
temperature_converter()
