#Exercise one
# Declare an empty list
empty_list = []

# Declare a list with more than 5 items
more_than_5_items = [1, 'apple', True, 3.14, 'python']

# Find the length of your list
length_of_list = len(more_than_5_items)

# Get the first item, the middle item, and the last item of the list
first_item = more_than_5_items[0]
middle_item = more_than_5_items[length_of_list // 2]
last_item = more_than_5_items[-1]

# Declare a list called mixed_data_types
mixed_data_types = ['YourName', 25, 5.8, 'Married', 'YourAddress']

# Declare a list variable named it_companies
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# Print the list
print(it_companies)

# Print the number of companies in the list
number_of_companies = len(it_companies)
print(number_of_companies)

# Print the first, middle, and last company
first_company = it_companies[0]
middle_company = it_companies[number_of_companies // 2]
last_company = it_companies[-1]
print(first_company, middle_company, last_company)

# Print the list after modifying one of the companies
it_companies[2] = 'Microsoft Corporation'
print(it_companies)

# Add an IT company to it_companies
it_companies.append('NewCompany')

# Insert an IT company in the middle of the companies list
it_companies.insert(number_of_companies // 2, 'InsertedCompany')

# Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[4] = it_companies[4].upper()

# Join the it_companies with a string '#;  '
joined_companies = '#;  '.join(it_companies)
print(joined_companies)

# Check if a certain company exists in the it_companies list
company_to_check = 'Facebook'
exists = company_to_check in it_companies
print(exists)

# Sort the list using sort() method
it_companies.sort()

# Reverse the list in descending order using reverse() method
it_companies.reverse()

# Slice out the first 3 companies from the list
first_3_companies = it_companies[:3]

# Slice out the last 3 companies from the list
last_3_companies = it_companies[-3:]

# Slice out the middle IT company or companies from the list
middle_company_index = number_of_companies // 2
middle_company = it_companies[middle_company_index] if number_of_companies % 2 != 0 else it_companies[middle_company_index - 1:middle_company_index + 1]

# Remove the first IT company from the list
it_companies.pop(0)

# Remove the middle IT company or companies from the list
it_companies.pop(middle_company_index)

# Remove the last IT company from the list
it_companies.pop()

# Remove all IT companies from the list
it_companies.clear()

# Destroy the IT companies list
del it_companies

# Join the following lists
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
full_stack = front_end + back_end

# Insert Python and SQL after Redux
full_stack.insert(full_stack.index('Redux') + 1, 'Python')
full_stack.insert(full_stack.index('Redux') + 2, 'SQL')

print(full_stack)
