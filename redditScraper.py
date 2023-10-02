import requests
from bs4 import BeautifulSoup
import nltk
from nltk.tokenize import sent_tokenize
import re
import os
nltk.download('punkt')

# Prompt the user for the Reddit URL
reddit_url = input("Enter the Reddit URL you want to scrape: ")

# Make an HTTP GET request to the URL
response = requests.get(reddit_url)

if response.status_code == 200:
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find and extract all user comments
    comments = soup.find_all("div", {"class": "md"})

    # Create a directory to store user-specific files
    output_directory = 'reddit_comments'
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    for comment in comments:
        # Extract the username and comment text
        user_tag = comment.find_previous("a", {"class": "author"})
        if user_tag:
            username = user_tag.text
            comment_text = comment.get_text()
            
            # Remove extra spaces and line breaks from the comment text
            comment_text = re.sub(r'\s+', ' ', comment_text).strip()

            # Create a file for each user and write their comments
            user_file_path = os.path.join(output_directory, f"{username}.txt")
            with open(user_file_path, 'a', encoding='utf-8') as user_file:
                user_file.write(comment_text + '\n')
    
    print(f"Data scraped and saved in the '{output_directory}' directory.")
else:
    print(f"Failed to fetch the Reddit page. Status code: {response.status_code}")
