# Create an empty dictionary called dog
dog = {}

# Add name, color, breed, legs, age to the dog dictionary
dog['name'] = 'Hope'
dog['color'] = 'Brown'
dog['breed'] = 'local'
dog['legs'] = 4
dog['age'] = 3

# Create a student dictionary
student = {
    'first_name': 'Mutala',
    'last_name': 'Jamal Deen',
    'gender': 'Male',
    'age': 25,
    'marital_status': 'Single',
    'skills': ['Python', 'Django'],
    'country': 'Ghana',
    'city': 'Tamale',
    'address': 'sakasaka 2'
}

# Get the length of the student dictionary
print("Length of student dictionary:", len(student))

# Get the value of skills and check the data type
skills_value = student['skills']
print("Skills:", skills_value)
print("Data type of skills:", type(skills_value))

# Modify the skills values by adding one or two skills
student['skills'].extend(['HTML', 'CSS'])

# Get the dictionary keys as a list
keys_list = list(student.keys())
print("Keys as a list:", keys_list)

# Get the dictionary values as a list
values_list = list(student.values())
print("Values as a list:", values_list)

# Change the dictionary to a list of tuples using items() method
items_list = list(student.items())
print("Items as a list of tuples:", items_list)

# Delete one of the items in the dictionary
del student['marital_status']

# Delete one of the dictionaries (dog)
del dog

# Print the modified student dictionary
print("Modified student dictionary:", student)
