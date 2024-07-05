def greet_user(name):
    # Function to greet the user
    print(f"Hello, {name}! Welcome to our program.")

def farewell_user(name):
    # Function to bid farewell to the user
    print(f"Goodbye, {name}! Have a great day.")

def main():
    # Main function to demonstrate greeting and farewell
    name = "Alice"  # Example user name
    greet_user(name)  # Call the greeting function
    farewell_user(name)  # Call the farewell function

if __name__ == "__main__":
    # Entry point of the program
    main()
