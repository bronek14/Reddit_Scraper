
# This Module's task is to import and call the functionality of Mod_2 and Mod_3, the expected imput will only be a link to a reddit thread (Ex. i have provided a sample link in the ReadMe),
#This will be prompted to the user when run.py is called 



import sys

sys.path.append('../Module_2')  # Add the path to Module_2 to the system path
sys.path.append('../Module_3')  # Add the path to Module_3 to the system path
import shutil

from redditScraper import scrape_and_save
from extract_comments import filter_and_save_comments

# Define the URL and output filename
url = input('Enter the URL you want to scrape: ')
output_filename = 'output.txt'

    # Call the scrape_and_save function
scrape_and_save(url, output_filename)


#shifting output data to Raw // Needs Refactoring
source_file= output_filename
destination_file = 'C:\\Users\\jdurl\\Reddit_Scraper\\CS325_p3\\Data\\Raw'

try:
        shutil.move(source_file, destination_file)                                
except FileNotFoundError:
        print(f'Error: "output.txt" not found in the current location.')



# Call the filter_and_save_comments function

input_filename = 'C:\\Users\\jdurl\\Reddit_Scraper\\CS325_p3\\Data\Raw\\output.txt'
output_file = 'comments.txt'
filter_and_save_comments(input_filename, output_file)

#shifting filtered data to Processed // Needs Refactoring
source_file= output_file
destination_file2 = 'C:\\Users\\jdurl\\Reddit_Scraper\\CS325_p3\\Data\\Processed'

try:
    shutil.move(source_file, destination_file2)
except FileNotFoundError:
    print(f'Error: "output.txt" not found in the current location.')
