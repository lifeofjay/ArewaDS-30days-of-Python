import re
#EXERCISE ONE
import re
from collections import Counter

paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'

# Find the most frequent word in the paragraph
word_counts = Counter(re.findall(r'\b\w+\b', paragraph.lower()))
most_frequent_word = max(word_counts, key=word_counts.get)

print(f"The most frequent word is: {most_frequent_word}")

# Calculate the distance between the two furthest particles
points_text = 'The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction.'
points = [int(point) for point in re.findall(r'-?\d+', points_text)]
sorted_points = sorted(points)
distance = sorted_points[-1] - sorted_points[0]

print(f"The distance between the two furthest particles is: {distance}")

#EXERCISE TWO


def is_valid_variable(variable_name):
    pattern = re.compile(r'^[a-zA-Z_][a-zA-Z0-9_]*$')
    return bool(pattern.match(variable_name))

# Test cases
print(is_valid_variable('first_name'))  # True
print(is_valid_variable('first-name'))  # False
print(is_valid_variable('1first_name'))  # False
print(is_valid_variable('firstname'))    # True


#EXERCISE THREE

from collections import Counter

def clean_text(text):
    cleaned_text = re.sub(r'[^a-zA-Z\s]', '', text)  # Remove non-alphabetic characters
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip()  # Remove extra whitespaces
    return cleaned_text.lower()  # Convert to lowercase

def most_frequent_words(text):
    words = text.split()
    word_counts = Counter(words)
    most_common_words = word_counts.most_common(3)
    return most_common_words

sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

cleaned_text = clean_text(sentence)
print(cleaned_text)
print(most_frequent_words(cleaned_text))
