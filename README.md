# Reddit_Scraper
This Programs purpose is to download the content of a Reddit thread and save that data to a text file

## Prerequisites 
- Anaconda 3
- Git
### Installing 
1. Begin by cloning the repository to your machine using Git:
   ``` git clone https://github.com/bronek14/Reddit_Scraper.git ```

2. cd to the repository "Reddit_Scraper"

3. Create an environment with the details of the listed yaml file
   ``` conda env create -f requirements.yaml ```

4. Activate the newly created environment
   ``` conda activate "Your named env" ```
### Running the Project
``` python redditScraper.py  [https://old.reddit.com/r/CBRNE/](https://old.reddit.com/r/CBRNE/comments/168fbpr/which_version_of_the_jcad_can_actually_detect/) output.txt ```

NOTE: You may use whatever thread URL you wish but the replace the "www." portion with "old." 
and "output.txt" is required, this is the location file to which the data will be save to.
