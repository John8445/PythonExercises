def factorial(num):
    if num <= 1:
        return num
    else:
        return num * factorial(num-1)
    

# Ask the user for a numerical input
user_input = input("Enter a number: ")

try:
    # Convert the input to an integer
    num = int(user_input)
    print(f"You entered an integer: {num}")

    # Calculate and print the factorial
    result = factorial(num)
    print(f"The factorial of {num} is: {result}")
except ValueError:
    # If the input cannot be converted to an integer
    print("Invalid input. Please enter a valid integer.")

