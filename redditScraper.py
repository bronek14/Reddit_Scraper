import requests
from bs4 import BeautifulSoup

# Function to scrape Reddit data from a URL and save it to a file
def scrape_reddit_data(url, output_file):
    try:
        # Send a GET request to the Reddit URL
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content of the page
            soup = BeautifulSoup(response.text, 'html.parser')

            # Find and extract the relevant data (e.g., post titles, comments)
            # Modify this part to extract the specific data you're interested in
            data_to_extract = []

            # Save the extracted data to the output file
            with open(output_file, 'w', encoding='utf-8') as file:
                for item in data_to_extract:
                    file.write(item + '\n')

            print(f"Data scraped and saved to {output_file}")
        else:
            print(f"Failed to retrieve data from {url}. Status code: {response.status_code}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    # Input Reddit URL
    reddit_url = input("Enter the Reddit URL: ")

    # Output file name
    output_file = "output.txt"

    # Call the function to scrape and save data
    scrape_reddit_data(reddit_url, output_file)
