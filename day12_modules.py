# Exercise one
import random

# Function to generate a random six-digit/character user ID
def random_user_id():
    return ''.join(random.choices('0123456789abcdef', k=6))

print(random_user_id())

# Function to generate user IDs based on user input
def user_id_gen_by_user():
    char_count, id_count = map(int, input("Enter the number of characters and number of IDs separated by a space: ").split())
    user_ids = [''.join(random.choices('abcdefghijklmnopqrstuvwxyz0123456789', k=char_count)) for _ in range(id_count)]
    return user_ids

print(user_id_gen_by_user())

# Function to generate a random RGB color
def rgb_color_gen():
    return f"rgb({random.randint(0, 255)}, {random.randint(0, 255)}, {random.randint(0, 255)})"

print(rgb_color_gen())
 
 # Exercise two


# Function to generate a list of hexadecimal colors
def list_of_hexa_colors(num_colors):
    hexa_colors = ['#' + ''.join(random.choices('0123456789abcdef', k=6)) for _ in range(num_colors)]
    return hexa_colors

# Function to generate a list of RGB colors
def list_of_rgb_colors(num_colors):
    def rgb_color_gen():
        return f"rgb({random.randint(0, 255)}, {random.randint(0, 255)}, {random.randint(0, 255)})"
    
    rgb_colors = [rgb_color_gen() for _ in range(num_colors)]
    return rgb_colors

# Function to generate any number of hexa or rgb colors
def generate_colors(color_type, num_colors):
    if color_type == 'hexa':
        return list_of_hexa_colors(num_colors)
    elif color_type == 'rgb':
        return list_of_rgb_colors(num_colors)

# Test cases
print(generate_colors('hexa', 3))
print(generate_colors('hexa', 1))
print(generate_colors('rgb', 3))
print(generate_colors('rgb', 1))
 #Exercise three


# Function to shuffle a list
def shuffle_list(input_list):
    shuffled_list = input_list.copy()
    random.shuffle(shuffled_list)
    return shuffled_list

# Function to generate an array of seven unique random numbers in a range of 0-9
def seven_unique_random_numbers():
    return random.sample(range(10), 7)

# Test cases
original_list = [1, 2, 3, 4, 5]
shuffled_result = shuffle_list(original_list)
print(f"Original List: {original_list}")
print(f"Shuffled List: {shuffled_result}")

seven_random_numbers_result = seven_unique_random_numbers()
print(f"Seven Unique Random Numbers: {seven_random_numbers_result}")
