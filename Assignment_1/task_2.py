def main():
    """
    Task 2: Personalized Greeting
    Takes first and last name as input and displays a welcome message.
    """
    # Get user input and strip any leading/trailing whitespace
    first_name = input("Enter your first name: ").strip()
    last_name = input("Enter your last name: ").strip()

    # Construct full name using f-string
    full_name = f"{first_name} {last_name}"

    # Display the greeting
    print(f"Hello {full_name}, Welcome to my GitHub Profile.")

if __name__ == "__main__":
    main()