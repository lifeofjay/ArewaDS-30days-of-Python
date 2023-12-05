# Exercise 1 
# Compare ages
your_age = int(input("Enter your age: "))
my_age = 30

if my_age > your_age:
    difference = my_age - your_age
    if difference == 1:
        print(f"You are {difference} year older than me.")
    else:
        print(f"You are {difference} years older than me.")
elif my_age < your_age:
    difference = your_age - my_age
    if difference == 1:
        print(f"You are {difference} year younger than me.")
    else:
        print(f"You are {difference} years younger than me.")
else:
    print("We are of the same age.")

# Compare two numbers
a = float(input("Enter number one: "))
b = float(input("Enter number two: "))

if a > b:
    print(f"{a} is greater than {b}.")
elif a < b:
    print(f"{a} is smaller than {b}.")
else:
    print(f"{a} is equal to {b}.")
 #Exercise 2
 # Grade assignment
score = int(input("Enter the student's score: "))

if 80 <= score <= 100:
    grade = 'A'
elif 70 <= score <= 89:
    grade = 'B'
elif 60 <= score <= 69:
    grade = 'C'
elif 50 <= score <= 59:
    grade = 'D'
elif 0 <= score <= 49:
    grade = 'F'
else:
    grade = 'Invalid score'

print(f"The student's grade is: {grade}")

# Season check
month = input("Enter the month: ").lower()

if month in ['september', 'october', 'november']:
    season = 'Autumn'
elif month in ['december', 'january', 'february']:
    season = 'Winter'
elif month in ['march', 'april', 'may']:
    season = 'Spring'
elif month in ['june', 'july', 'august']:
    season = 'Summer'
else:
    season = 'Invalid month'

print(f"The season in {month.capitalize()} is: {season}")

# Fruits list
fruits = ['banana', 'orange', 'mango', 'lemon']
new_fruit = input("Enter a fruit to check or add to the list: ").lower()

if new_fruit in fruits:
    print("That fruit already exists in the list.")
else:
    fruits.append(new_fruit)
    print("Modified fruit list:", fruits)
#Exercise 3
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

# Check if the person dictionary has skills key
if 'skills' in person:
    skills_list = person['skills']
    
    # Print out the middle skill in the skills list
    if len(skills_list) % 2 == 1:
        middle_skill = skills_list[len(skills_list) // 2]
        print(f"The middle skill is: {middle_skill}")

    # Check if the person has 'Python' skill and print the result
    if 'Python' in skills_list:
        print("The person has the 'Python' skill.")

    # Check for developer roles based on skills
    if skills_list == ['JavaScript', 'React']:
        print("He is a front-end developer.")
    elif set(['Node', 'Python', 'MongoDB']).issubset(skills_list):
        print("He is a backend developer.")
    elif set(['React', 'Node', 'MongoDB']).issubset(skills_list):
        print("He is a fullstack developer.")
    else:
        print("Unknown title.")

# If the person is married and lives in Finland
if person.get('is_married') and person.get('country') == 'Finland':
    print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is married.")
