import requests
from collections import Counter
from bs4 import BeautifulSoup
import re
import statistics


# Specify the URL for text content
text_url = 'http://www.gutenberg.org/files/1112/1112.txt'

# Make a GET request to the URL
response = requests.get(text_url)
html_content = response.content

# Parse HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Extract text content from HTML
text_content = soup.get_text()

# Remove non-alphabetic characters and convert to lowercase
cleaned_text = re.sub(r'[^a-zA-Z\s]', '', text_content).lower()

# Split the text into words
word_list = cleaned_text.split()

# Count the frequency of each word
word_counts = Counter(word_list)

# Get the 10 most frequent words
top_10_words = word_counts.most_common(10)

print("The 10 most frequent words:")
for word, count in top_10_words:
    print(f"{word} - {count}")


# Read the cats API and cats_api = 'https://api.thecatapi.com/v1/breeds' and find :
#the min, max, mean, median, standard deviation of cats' weight in metric units.
#the min, max, mean, median, standard deviation of cats' lifespan in years.
#Create a frequency table of country and breed of cats




# Specify the URL for cat breeds data
cats_api_url = 'https://api.thecatapi.com/v1/breeds'

# Make a GET request to the cat breeds API
response = requests.get(cats_api_url)
cat_data = response.json()

# Extract cat weights from the data
cat_weights = [float(cat['weight']['metric'].split()[0]) for cat in cat_data]

# Calculate statistical measures
min_weight = min(cat_weights)
max_weight = max(cat_weights)
mean_weight = statistics.mean(cat_weights)
median_weight = statistics.median(cat_weights)
std_dev_weight = statistics.stdev(cat_weights)

print("Statistical measures of cats' weight in metric units:")
print("Minimum Weight:", min_weight)
print("Maximum Weight:", max_weight)
print("Mean Weight:", mean_weight)
print("Median Weight:", median_weight)
print("Standard Deviation of Weight:", std_dev_weight)



# Specify the URL for cat breeds data
cats_api_url = 'https://api.thecatapi.com/v1/breeds'

# Make a GET request to the cat breeds API
response = requests.get(cats_api_url)
cat_data = response.json()

# Extract and filter cat lifespans
cat_lifespans = [float(cat['life_span'].split()[0]) for cat in cat_data if 'life_span' in cat and cat['life_span']]

# Calculate statistical measures
min_lifespan = min(cat_lifespans)
max_lifespan = max(cat_lifespans)
mean_lifespan = statistics.mean(cat_lifespans)
median_lifespan = statistics.median(cat_lifespans)
std_dev_lifespan = statistics.stdev(cat_lifespans)

# Display the results
print("Statistical measures of cats' lifespan in years:")
print("Minimum Lifespan:", min_lifespan)
print("Maximum Lifespan:", max_lifespan)
print("Mean Lifespan:", mean_lifespan)
print("Median Lifespan:", median_lifespan)
print("Standard Deviation of Lifespan:", std_dev_lifespan)


# Specify the URL for cat breeds data
cats_api_url = 'https://api.thecatapi.com/v1/breeds'

# Make a GET request to the cat breeds API
response = requests.get(cats_api_url)
cat_data = response.json()

# Create a frequency table for country and breed
frequency_table = Counter()

# Iterate over the data and count occurrences of each country and breed
for cat in cat_data:
    country = cat.get('origin', 'Unknown')
    breed = cat.get('name', 'Unknown')
    frequency_table[(country, breed)] += 1

# Display the frequency table
print("Frequency table of country and breed of cats:")
for (country, breed), count in frequency_table.items():
    print(f"Country: {country} - Breed: {breed} - Count: {count}")
    

# Specify the URL for countries data
countries_api_url = 'https://restcountries.eu/rest/v2/all'

# Make a GET request to the countries API
response = requests.get(countries_api_url)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()

    # Sort the countries based on land area in descending order
    sorted_countries = sorted(data, key=lambda country: country.get('area', 0), reverse=True)

    # Get the 10 largest countries
    largest_countries = sorted_countries[:10]

    # Display the 10 largest countries
    print("10 Largest Countries:")
    for country in largest_countries:
        print(f"{country['name']} - {country.get('area', 'N/A')} sq km")
else:
    print(f"Error: Unable to access the countries API. Status Code: {response.status_code}")
    
# Specify the URL for the UCI dataset page
uci_url = 'https://archive.ics.uci.edu/ml/datasets.php'

# Make a GET request to the UCI dataset page
response = requests.get(uci_url)

# Check if the request was successful
if response.status_code == 200:
    # Create a BeautifulSoup object to parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the table containing the dataset information
    table = soup.find('table', {'border': '1'})

    # Iterate over each row in the table
    for row in table.find_all('tr'):
        # Extract the dataset name and link from the table cells
        cells = row.find_all('td')
        if len(cells) > 0:
            dataset_name = cells[0].text.strip()
            dataset_link = cells[0].find('a')['href']
            print(f"Dataset Name: {dataset_name}")
            print(f"Dataset Link: {dataset_link}")
            print('---')
else:
    print(f"Error: Unable to access the UCI dataset page. Status Code: {response.status_code}")


