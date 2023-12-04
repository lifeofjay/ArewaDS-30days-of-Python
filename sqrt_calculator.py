# Get user input for the number
user_input = input("Enter a number to calculate its square root: ")

# Convert the input to a floating-point number
try:
    number = float(user_input)
except ValueError:
    print("Invalid input. Please enter a valid number.")
    exit()

# Check if the number is non-negative
if number < 0:
    print("Cannot calculate square root of a negative number.")
else:
    # Calculate and display the square root
    square_root = number ** 0.5
    print("The square root of {} is: {}".format(number, square_root))
