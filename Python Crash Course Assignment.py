#Exercise 8.1
"""Write a function called display_message() that prints one sentence telling everyone what you are learning about in this chapter. Call the 
function, and make sure the message displays correctly"""
def display_message():
    print("In this chapter, we are learning about functions in Python.")
display_message()
#Exercise 8.1
"""Write a function called favorite_book() that accepts one 
parameter, title. The function should print a message, such as One of my 
favorite books is Alice in Wonderland. Call the function, making sure to 
include a book title as an argument in the function call.""" 
def favorite_book(title):
    print(f"One of my favorite books is {title}.")
favorite_book("Alice in Wonderland")
#EXERCISE 8.3
"""Write a function called make_shirt() that accepts a size and the 
text of a message that should be printed on the shirt. The function should print a 
sentence summarizing the size of the shirt and the message printed on it.
Call the function once using positional arguments to make a shirt. Call the 
function a second time using keyword arguments.""" 
def make_shirt(size, message):
    print(f"I'm making an {size} shirt with the message '{message}' printed on it.")
make_shirt("M", "Python is my favorite!")

make_shirt(message="Coding is fun!", size="XL")
#EXERCISE 8.4
"""Modify the make_shirt() function so that shirts are large 
by default with a message that reads I love Python. Make a large shirt and a 
medium shirt with the default message, and a shirt of any size with a different 
message""" 
def make_shirt(size="L", message="Python is my favourite!"):
    print(f"I'm making a {size} shirt with the message '{message}' printed on it.")
make_shirt()
make_shirt(size="M")
make_shirt(message="Coding is fun!", size="XL")
#EXERCISE 8.5
"""Write a function called describe_city() that accepts the name of 
a city and its country. The function should print a simple sentence, such as 
Reykjavik is in Iceland. Give the parameter for the country a default value. 
Call your function for three different cities, at least one of which is not in the 
default country."""
def describe_city(city_name, country="Iceland"):
    print(f"{city_name.title()} is in {country.title()}.")
describe_city("reykjavik")
describe_city("tokyo", country="japan")
describe_city("paris", country="france")
#EXERCISE 8.6
"""Write a function called city_country() that takes in the name 
of a city and its country. The function should return a string formatted like this:
"Santiago, Chile"
Call your function with at least three city-country pairs, and print the values 
that are returned.""" 
def city_country(city_name, country):
    return f"{city_name.title()}, {country.title()}"
print(city_country("santiago", "chile"))
print(city_country("london", "england"))
print(city_country("tokyo", "japan"))
#EXERCISE 8.7
"""Write a function called make_album() that builds a dictionary 
describing a music album. The function should take in an artist name and an 
album title, and it should return a dictionary containing these two pieces of 
information. Use the function to make three dictionaries representing different 
albums. Print each return value to show that the dictionaries are storing the 
album information correctly.
Use None to add an optional parameter to make_album() that allows you to 
store the number of songs on an album. If the calling line includes a value for 
the number of songs, add that value to the album’s dictionary. Make at least 
one new function call that includes the number of songs on an album.""" 
def make_album(artist_name, album_title, num_songs=None):
    album_dict = {
      "artist": artist_name.title(),
      "album": album_title.title(),
  }
    if num_songs:
        album_dict["songs"] = num_songs
    return album_dict

album1 = make_album("kendrick lamar", "to pimp a butterfly")
album2 = make_album("beyoncé", "lemonade")
album3 = make_album("taylor swift", "folklore", 16)
print(album1)
print(album2)
print(album3)
#EXERCISE 8.8
"""Write a while loop that allows users to enter an album’s artist and title. Once you have that 
information, call make_album() with the user’s input and print the dictionary 
that’s created. Be sure to include a quit value in the while loop""" 
def make_album(artist, title):
    """Create a dictionary representing an album."""
    album_info = {'artist': artist, 'title': title}
    return album_info

while True:
    artist = input("Enter the artist's name (or 'quit' to exit): ")
    
    if artist.lower() == 'quit':
        break
    
    title = input("Enter the album title: ")

    album = make_album(artist, title)
    print("Album information:")
    print(album)
    break
#EXERCISE 8.9
"""Make a list containing a series of short text messages. Pass the 
list to a function called show_messages(), which prints each text message""" 
def show_messages(messages):
    for message in messages:
        print(message)
text_messages = [
    "Hello, how are you?",
    "Don't forget to buy groceries.",
    "Meeting at 2 PM in the conference room.",
    "It's new year!",
    "Happy new year!",
]
show_messages(text_messages)
#EXERCISE 8.10
"""Start with a copy of your program from Exercise 8-9. 
Write a function called send_messages() that prints each text message and 
moves each message to a new list called sent_messages as it’s printed. After 
calling the function, print both of your lists to make sure the messages were 
moved correctly""" 
def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop(0)
        print("Sending message: ", current_message)
        sent_messages.append(current_message)
text_messages = [
    "Hello, how are you?",
    "Don't forget to buy groceries.",
    "Meeting at 2 PM in the conference room.",
    "It's new year!",
    "Happy new year!",
]
sent_messages = []
send_messages(text_messages, sent_messages)

print("Original messages:")
print(text_messages)

print("\nSent messages:")
print(sent_messages)
#EXERCISE 8.11
"""Start with your work from Exercise 8-10. Call the function
send_messages() with a copy of the list of messages. 
After calling the function, print both of your lists to show that 
the original list has retained its messages.""" 
def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop(0)
        print("Sending message: ", current_message)
        sent_messages.append(current_message)
        
text_messages = [
    "Hello, how are you?",
    "Don't forget to buy groceries.",
    "Meeting at 2 PM in the conference room.",
    "It's new year!",
    "Happy new year!",
]

messages_copy = text_messages.copy()

sent_messages = []

send_messages(messages_copy, sent_messages)

print("Original messages:")
print(text_messages)

print("\nSent messages:")
print(sent_messages)
#EXERCISE 8.12
"""Write a function that accepts a list of items a person wants 
on a sandwich. The function should have one parameter that collects as many 
items as the function call provides, and it should print a summary of the sandwich 
that’s being ordered. Call the function three times, using a different number of arguments each time""" 
def make_sandwich(*items):
    print("Making a sandwich with the following items:")
    for item in items:
        print("- " + item)
    print("Sandwich is ready!\n")

make_sandwich("Ham", "Cheese", "Lettuce")
make_sandwich("Turkey", "Swiss", "Tomato", "Mayo")
make_sandwich("Peanut Butter", "Jelly")
#EXERCISE 8.13
"""Start with a copy of user_profile.py from page 148. Build a 
profile of yourself by calling build_profile(), using your first and last names 
and three other key-value pairs that describe you""" 
def build_profile(first_name, last_name, **additional_info):
    profile = {'first_name': first_name, 'last_name': last_name}
    for key, value in additional_info.items():
        profile[key] = value
    return profile

my_profile = build_profile(
    first_name="Jamal",
    last_name="Deen",
    age=21,
    occupation="Computer Scientist",
    hobbies=["Reading", "Coding", "Learning"]
)
print(my_profile)
#EXERCISE 8.14
"""Write a function that stores information about a car in a dictionary. The function should always receive a manufacturer and a model name. It 
should then accept an arbitrary number of keyword arguments. Call the function with the required information and two other name-value pairs, such as a 
color or an optional feature. Your function should work for a call like this one:
car = make_car('subaru', 'outback', color='blue', tow_package=True)
Print the dictionary that’s returned to make sure all the information was 
stored correctly""" 
def make_car(manufacturer, model, **kwargs):
    car_info = {'manufacturer': manufacturer, 'model': model}
    car_info.update(kwargs)
    return car_info
car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)
#EXERCISE 8.15
from printing_functions import print_models, show_completed_models

designs_to_print = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(designs_to_print, completed_models)
show_completed_models(completed_models)   
#EXERCISE 8.16
"""Using a program you wrote that has one function in it, store that 
function in a separate file. Import the function into your main program file, and 
call the function using each of these approaches:
import module_name
from module_name import function_name
from module_name import function_name as fn
import module_name as mn
from module_name import *""" 
import my_functions

my_functions.say_hello()  

from my_functions import say_hello

say_hello() 

from my_functions import say_hello as greet

greet() 

import my_functions as mf

mf.say_hello()  

from my_functions import *

say_hello()
#EXERCISE 8.17
"""Choose any three programs you wrote for this chapter, 
and make sure they follow the styling guidelines described in this section.""" 
def make_sandwich(*ingredients):
    print("Making a sandwich with the following ingredients:")
    for ingredient in ingredients:
        print("- " + ingredient)
    print("Sandwich is ready!\n")
    
make_sandwich("Ham", "Cheese", "Lettuce")
make_sandwich("Turkey", "Swiss", "Tomato", "Mayo")
make_sandwich("Peanut Butter", "Jelly")