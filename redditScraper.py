import requests
from bs4 import BeautifulSoup
import nltk
from nltk.tokenize import word_tokenize
nltk.download('punkt')

# Define the Reddit URL you want to scrape
reddit_url = 'https://www.reddit.com/r/Python/comments/'

# Make an HTTP GET request to the URL
response = requests.get(reddit_url)

if response.status_code == 200:
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find and extract the text content
    page_text = soup.get_text()
    
    # Tokenize the text into words using NLTK
    words = word_tokenize(page_text)
    
    # Filter out non-alphanumeric words and convert to lowercase
    words = [word.lower() for word in words if word.isalnum()]
    
    # Create a set of unique words to remove duplicates
    unique_words = set(words)
    
    # Write the words to the output.txt file
    with open('output.txt', 'w', encoding='utf-8') as output_file:
        output_file.write('\n'.join(unique_words))
    
    print(f"Data scraped and saved to 'output.txt'.")
else:
    print(f"Failed to fetch the Reddit page. Status code: {response.status_code}")
