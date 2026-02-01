def main():
    """
    Task 1: Basic Arithmetic Operations
    Takes two integer inputs from the user and performs addition,
    subtraction, multiplication, and division.
    """
    try:
        # Get input from user with clear prompts
        num1 = int(input("Enter the value of a: "))
        num2 = int(input("Enter the value of b: "))

        # Perform and display calculations using f-strings for readability
        print(f"Addition: {num1 + num2}")
        print(f"Subtraction: {num1 - num2}")
        print(f"Multiplication: {num1 * num2}")

        # Check for division by zero to prevent crashing
        if num2 != 0:
            print(f"Division: {num1 / num2}")
        else:
            print("Division: undefined (division by zero)")

    except ValueError:
        print("Error: Please enter valid integer numbers.")

if __name__ == "__main__":
    main()
