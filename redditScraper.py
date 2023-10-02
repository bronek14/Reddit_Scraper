import requests
from bs4 import BeautifulSoup
import argparse

def scrape_reddit_thread(url, output_file="output.txt"):
    try:
        # Send an HTTP GET request to the Reddit thread URL
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content of the page
            soup = BeautifulSoup(response.text, 'html.parser')

            # Find all comments and replies
            comments = soup.find_all("div", {"class": "comment"})

            # Extract text from comments and replies
            comment_texts = []
            for comment in comments:
                comment_text = comment.find("div", {"class": "md"})
                if comment_text:
                    comment_texts.append(comment_text.get_text())

            # Combine all comments into a single string
            thread_data = "\n\n".join(comment_texts)

            # Save the data to the output file
            with open(output_file, "w", encoding="utf-8") as file:
                file.write(thread_data)

            print(f"Scraped data successfully and saved to {output_file}")
        else:
            print(f"Failed to retrieve the Reddit thread. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def main():
    parser = argparse.ArgumentParser(description='Scrape data from a Reddit thread.')
    parser.add_argument('url', type=str, help='URL of the Reddit thread to scrape')
    parser.add_argument('--output', type=str, default='output.txt', help='Output file name (default: output.txt)')
    args = parser.parse_args()

    scrape_reddit_thread(args.url, args.output)

if __name__ == '__main__':
    main()
