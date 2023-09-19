import argparse
import requests
from bs4 import BeautifulSoup

def download_text_content(url, output_file):
    try:
        # Send an HTTP GET request to the URL
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content of the page using BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')

            # Extract text data from the page
            text_data = soup.get_text()

            # Write the text data to the output file
            with open(output_file, 'w', encoding='utf-8') as file:
                file.write(text_data)

            print(f"Text content downloaded and saved to {output_file}")
        else:
            print(f"Failed to retrieve content. Status code: {response.status_code}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

def main():
    parser = argparse.ArgumentParser(description="Download text content from a URL")
    parser.add_argument("URL", help="The URL to download text content from")
    parser.add_argument("output_file", help="The name of the output text file")

    args = parser.parse_args()
    download_text_content(args.URL, args.output_file)

if __name__ == "__main__":
    main()
