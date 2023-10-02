import requests
from bs4 import BeautifulSoup

# Function to scrape a Reddit thread and save it to a text file
def scrape_reddit_thread(url, output_file):
    try:
        # Send a GET request to the Reddit thread URL
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            # Find all the comment elements
            comments = soup.find_all(class_='comment')

            # Open the output file for writing
            with open(output_file, 'w', encoding='utf-8') as file:
                for comment in comments:
                    # Extract and write the text of each comment to the file
                    comment_text = comment.find(class_='md').get_text()
                    file.write(comment_text)
                    file.write('\n\n')

            print(f"Scraped data from {len(comments)} comments and saved to {output_file}")
        else:
            print(f"Failed to fetch data from {url}. Status code: {response.status_code}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

