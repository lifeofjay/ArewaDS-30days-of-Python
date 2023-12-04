# Create an empty tuple
empty_tuple = ()

# Create a tuple containing names of your sisters and your brothers
sisters = ('Abibata', 'Fadilatu')
brothers = ('Gafaru', 'Musherife', 'Sudais')

# Join brothers and sisters tuples and assign it to siblings
siblings = brothers + sisters

# How many siblings do you have?
number_of_siblings = len(siblings)

# Modify the siblings tuple and add the name of your father and mother
family_members = ('Mr.Mutala', 'Hajia Zuweira') + siblings
 
 #Exercise two
 
# Unpack siblings and parents from family_members
father, mother, *siblings = family_members

# Create fruits, vegetables, and animal products tuples
fruits = ('Apple', 'Banana', 'Orange')
vegetables = ('Carrot', 'Broccoli', 'Spinach')
animal_products = ('Chicken', 'Beef', 'Eggs')

# Join the three tuples and assign it to a variable called food_stuff_tp
food_stuff_tp = fruits + vegetables + animal_products

# Change the food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)

# Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list
middle_items_tp = food_stuff_tp[len(food_stuff_tp)//2]
middle_items_lt = food_stuff_lt[len(food_stuff_lt)//2]

# Slice out the first three items and the last three items from the food_stuff_lt list
first_three_items = food_stuff_lt[:3]
last_three_items = food_stuff_lt[-3:]

# Delete the food_staff_tp tuple completely
del food_stuff_tp

# Check if an item exists in tuple
# Check if 'Estonia' is a Nordic country
nordic_countries = ('Sweden', 'Norway', 'Denmark', 'Finland', 'Iceland')
estonia_is_nordic = 'Estonia' in nordic_countries

# Check if 'Iceland' is a Nordic country
iceland_is_nordic = 'Iceland' in nordic_countries