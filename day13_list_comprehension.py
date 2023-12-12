# Task 1: Filter only negative and zero in the list using list comprehension
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
filtered_numbers = [num for num in numbers if num <= 0]
print(filtered_numbers)

# Task 2: Flatten the list of lists of lists to a one-dimensional list
list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flattened_list = [num for sublist in list_of_lists for subsublist in sublist for num in subsublist]
print(flattened_list)

# Task 3: Create a list of tuples using list comprehension
tuple_list = [(i, 1, i, i**2, i**3, i**4, i**5) for i in range(11)]
print(tuple_list)

# Task 4: Flatten the list to a new list
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
flattened_countries = [[country.upper(), country[:3].upper(), city.upper()] for country, city in sum(countries, [])]
print(flattened_countries)

# Task 5: Change the list to a list of dictionaries
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
dict_countries = [{'country': country.upper(), 'city': city.upper()} for country, city in sum(countries, [])]
print(dict_countries)

# Task 6: Change the list of lists to a list of concatenated strings
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
concatenated_names = [' '.join(name) for name in sum(names, [])]
print(concatenated_names)

# Task 7: Lambda function for slope or y-intercept of linear functions
linear_function = lambda x, slope, y_intercept: slope * x + y_intercept
# Example usage: linear_function(3, 2, 1) would represent the linear function y = 2x + 1
