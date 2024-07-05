def square(number):
    # Function to calculate the square of a number
    result = number * number
    print(f"The square of {number} is {result}")
    return result

def cube(number):
    # Function to calculate the cube of a number
    result = number * number * number
    print(f"The cube of {number} is {result}")
    return result

def main():
    # Main function to demonstrate square and cube calculations
    number = 3  # Example number to calculate square and cube
    square(number)  # Call the square function
    cube(number)  # Call the cube function

if __name__ == "__main__":
    # Entry point of the program
    main()
