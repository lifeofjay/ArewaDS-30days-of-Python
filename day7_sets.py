# Exercise 1
# Initial set
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

# Length of the set
length_of_set = len(it_companies)
print("Length of it_companies:", length_of_set)

# Add 'Twitter' to it_companies
it_companies.add('Twitter')
print("After adding 'Twitter':", it_companies)

# Insert multiple IT companies at once
it_companies.update({'LinkedIn', 'Salesforce', 'Uber'})
print("After inserting multiple IT companies:", it_companies)

# Remove one of the companies
it_companies.remove('Twitter')
print("After removing 'Twitter':", it_companies)

# Difference between remove and discard
# Remove - Raises an error if the element is not present
# Discard - Does nothing if the element is not present

# Example using remove
try:
    it_companies.remove('Twitter')
except KeyError as e:
    print(f"Error: {e}")

# Example using discard
it_companies.discard('Twitter')

#Exercise 2
# Define sets A and B
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

# Join A and B
union_result = A.union(B)
print("Union of A and B:", union_result)

# Find A intersection B
intersection_result = A.intersection(B)
print("Intersection of A and B:", intersection_result)

# Check if A is a subset of B
is_subset = A.issubset(B)
print("A is a subset of B:", is_subset)

# Check if A and B are disjoint sets
are_disjoint = A.isdisjoint(B)
print("A and B are disjoint sets:", are_disjoint)

# Join A with B and B with A
join_AB = A.union(B)
join_BA = B.union(A)
print("Join A with B:", join_AB)
print("Join B with A:", join_BA)

# Symmetric difference between A and B
symmetric_difference = A.symmetric_difference(B)
print("Symmetric difference between A and B:", symmetric_difference)

# Delete the sets completely
del A
del B

#EXERCISE 3
ages = [22, 19, 24, 25, 26, 24, 25, 24]

# Convert ages to a set
ages_set = set(ages)

# Compare lengths
length_list = len(ages)
length_set = len(ages_set)

print("Length of the list:", length_list)
print("Length of the set:", length_set)

if length_set > length_list:
    print("The set has more unique elements than the list.")
elif length_set < length_list:
    print("The list has more unique elements than the set.")
else:
    print("The list and set have the same number of unique elements.")
 
 
 #Explain the Difference Between String, List, Tuple, and Set:

#String: An ordered sequence of characters. Immutable, meaning you cannot change the characters once the string is created.
#List: An ordered sequence of items. Mutable, meaning you can add, remove, or modify elements after the list is created.
#Tuple: Similar to a list but immutable. Once a tuple is created, you cannot change its elements.
#Set: An unordered collection of unique elements. Sets do not allow duplicate values.

sentence = "I am a teacher, and I love to inspire and teach people."

# Use split and set to get unique words
words = sentence.split()
unique_words = set(words)
print("Number of unique words:", len(unique_words))
