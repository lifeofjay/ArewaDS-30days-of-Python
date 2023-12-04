# Concatenate strings
string1 = 'Thirty'
string2 = 'Days'
string3 = 'Of'
string4 = 'Python'
concatenated_string = f'{string1} {string2} {string3} {string4}'
print(concatenated_string)

# Concatenate another set of strings
string5 = 'Coding'
string6 = 'For'
string7 = 'All'
another_string = f'{string5} {string6} {string7}'
print(another_string)

# Declare a variable and print it
company = "Coding For All"
print(company)

# Print the length of the company string
print(len(company))

# Convert characters to uppercase and lowercase
uppercase_company = company.upper()
lowercase_company = company.lower()
print(uppercase_company)
print(lowercase_company)

# Format the string using different methods
capitalized_company = company.capitalize()
title_case_company = company.title()
swapped_case_company = company.swapcase()
print(capitalized_company)
print(title_case_company)
print(swapped_case_company)

# Cut out the first word
first_word_cut = company.split(' ', 1)[1]
print(first_word_cut)

# Check if the string contains a word
contains_coding = 'Coding' in company
print(contains_coding)

# Replace a word in the string
replaced_string = company.replace('Coding', 'Python')
print(replaced_string)

# Replace another phrase in the string
updated_string = replaced_string.replace('Python For Everyone', 'Python for All')
print(updated_string)

# Split the string using space as a separator
split_company = company.split()
print(split_company)

# Split another string at the comma
tech_companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
split_tech_companies = tech_companies.split(', ')
print(split_tech_companies)

# Access characters by index
first_char = company[0]
index_10_char = company[10]
last_index = company[-1]
print(first_char)
print(index_10_char)
print(last_index)

# Create acronyms
acronym_python = ''.join(word[0] for word in 'Python For Everyone'.split())
acronym_coding = ''.join(word[0] for word in 'Coding For All'.split())
print(acronym_python)
print(acronym_coding)

# Use index to determine positions
position_C = company.index('C')
position_F = company.index('F')
last_occurrence_l = company.rfind('l')
position_because = "You cannot end a sentence with because because because is a conjunction".find('because')

# Use rindex to find the last occurrence
last_occurrence_because = "You cannot end a sentence with because because because is a conjunction".rindex('because')

# Slice out a phrase
because_phrase = "You cannot end a sentence with because because because is a conjunction"[29:59]

# Check if a string starts or ends with a substring
starts_with_coding = company.startswith('Coding')
ends_with_coding = company.endswith('coding')

# Remove trailing spaces
trimmed_string = '   Coding For All      '.strip()

# Check isidentifier method
identifier_check_1 = '30DaysOfPython'.isidentifier()
identifier_check_2 = 'thirty_days_of_python'.isidentifier()

# Join a list with a hash with space string
python_libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
joined_libraries = ' # '.join(python_libraries)

# New line escape sequence
new_line_separated = 'I am enjoying this challenge.\nI just wonder what is next.'

# Tab escape sequence
tab_separated = 'Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki'

# String formatting method
radius = 10
area = 3.14 * radius ** 2
formatted_circle = f'The area of a circle with radius {radius} is {area} meters square.'

# String formatting for mathematical operations
addition_result = f'8 + 6 = {8 + 6}'
subtraction_result = f'8 - 6 = {8 - 6}'
multiplication_result = f'8 * 6 = {8 * 6}'
division_result = f'8 / 6 = {8 / 6}'
modulo_result = f'8 % 6 = {8 % 6}'
floor_division_result = f'8 // 6 = {8 // 6}'
exponential_result = f'8 ** 6 = {8 ** 6}'

# Print the results
print(position_C)
print(position_F)
print(last_occurrence_l)
print(position_because)
print(last_occurrence_because)
print(because_phrase)
print(starts_with_coding)
print(ends_with_coding)
print(trimmed_string)
print(identifier_check_1)
print(identifier_check_2)
print(joined_libraries)
print(new_line_separated)
print(tab_separated)
print(formatted_circle)
print(addition_result)
print(subtraction_result)
print(multiplication_result)
print(division_result)
print(modulo_result)
print(floor_division_result)
print(exponential_result)
