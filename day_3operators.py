# Declare variables
age = 25
height = 5.8
complex_number = 3 + 4j

# Task 1: Calculate area of a triangle
base = float(input("Enter the base of the triangle: "))
height_triangle = float(input("Enter the height of the triangle: "))
area_triangle = 0.5 * base * height_triangle
print(f"The area of the triangle is {area_triangle}")

# Task 2: Calculate perimeter of a triangle
side_a = float(input("Enter side a of the triangle: "))
side_b = float(input("Enter side b of the triangle: "))
side_c = float(input("Enter side c of the triangle: "))
perimeter_triangle = side_a + side_b + side_c
print(f"The perimeter of the triangle is {perimeter_triangle}")

# Task 3: Calculate area and perimeter of a rectangle
length_rectangle = float(input("\nEnter the length of the rectangle: "))
width_rectangle = float(input("Enter the width of the rectangle: "))
area_rectangle = length_rectangle * width_rectangle
perimeter_rectangle = 2 * (length_rectangle + width_rectangle)
print(f"The area of the rectangle is {area_rectangle}")
print(f"The perimeter of the rectangle is {perimeter_rectangle}")

# Task 4: Calculate area and circumference of a circle
radius_circle = float(input("\nEnter the radius of the circle: "))
pi = 3.14
area_circle = pi * (radius_circle ** 2)
circumference_circle = 2 * pi * radius_circle
print(f"The area of the circle is {area_circle}")
print(f"The circumference of the circle is {circumference_circle}")

# Task 5: Calculate slope, x-intercept, and y-intercept of y = 2x - 2
slope = 2
x_intercept = -2 / slope
y_intercept = -2
print(f"\nSlope: {slope}, X-intercept: {x_intercept}, Y-intercept: {y_intercept}")

# Task 6: Calculate slope and Euclidean distance between two points
x1, y1 = 2, 2
x2, y2 = 6, 10
slope_points = (y2 - y1) / (x2 - x1)
euclidean_distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
print(f"Slope between points: {slope_points}")
print(f"Euclidean distance between points: {euclidean_distance}")

# Task 7: Compare slopes
if slope == slope_points:
    print("The slopes are equal.")
else:
    print("The slopes are not equal.")

# Task 8: Calculate y value for different x values
x_values = [1, 2, 3, 4, 5]
y_values = [(x ** 2 + 6 * x + 9) for x in x_values]
print("\nCalculated y values for different x values:", y_values)

# Task 9: Falsy comparison statement
length_python = len('python')
length_dragon = len('dragon')
falsy_comparison = length_python == length_dragon
print(f"Falsy comparison statement: {falsy_comparison}")

# Task 10: Use 'and' operator to check if 'on' is found in both 'python' and 'dragon'
check_on = 'on' in 'python' and 'on' in 'dragon'
print(f"\n'On' is found in both 'python' and 'dragon': {check_on}")

# Task 11: Use 'in' operator to check if 'jargon' is in the sentence
sentence = "I hope this course is not full of jargon."
check_jargon = 'jargon' in sentence
print(f"\n'Jargon' is in the sentence: {check_jargon}")

# Task 12: Convert length of 'python' to float and then to string
length_python_float = float(length_python)
length_python_str = str(length_python_float)
print(f"\nLength of 'python' as float and then as string: {length_python_str}")

# Task 13: Check if a number is even
num_even = 10
is_even = num_even % 2 == 0
print(f"\nIs {num_even} even? {is_even}")

# Task 14: Check if floor division of 7 by 3 is equal to the int converted value of 2.7
floor_division_check = 7 // 3 == int(2.7)
print(f"\nIs floor division of 7 by 3 equal to int(2.7)? {floor_division_check}")

# Task 15: Check if type of '10' is equal to type of 10
type_check = type('10') == type(10)
print(f"\nIs type of '10' equal to type of 10? {type_check}")

# Task 16: Check if int('9.8') is equal to 10
int_conversion_check = int('9.8') == 10
print(f"\nIs int('9.8') equal to 10? {int_conversion_check}")

# Task 17: Calculate pay based on hours and rate per hour
hours_worked = float(input("\nEnter hours worked: "))
rate_per_hour = float(input("Enter rate per hour: "))
weekly_earning = hours_worked * rate_per_hour
print(f"Your weekly earning is {weekly_earning}")

# Task 18: Calculate number of seconds a person can live
years_lived = int(input("\nEnter number of years you have lived: "))
seconds_lived = years_lived * 365 * 24 * 60 * 60
print(f"You have lived for {seconds_lived} seconds.")

# Task 19: Display the table
print("\nDisplaying the table:")
for i in range(1, 6):
    print(i, 1, i, i**2, i**3)
