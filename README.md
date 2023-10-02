# Reddit_Scraper
This Programs purpose is to download the content of a Reddit thread and save that data to a text file, with options to extract only the comment data if needed.

## Prerequisites 
- Anaconda 3
- Git
  
### Installing 
1. Begin with creating an envrionment using the command ```conda create --name myenv```.
      - The "myenv" portion being whatever you want to name your envronment. Example: conda create --name Project.
        
2. Activate your newly created environment using ```conda activate ``` followed by the name of the env you created.
   
3. Now use the command ```conda install git``` which will allow you to use git commands to pull files from a repository.

4. Once your environment is activated and git is installed  you can use the command  ```git pull https://github.com/bronek14/Reddit_Scraper```
   to pull the files from this repository

5. Once the repository is pulled you should check your directory using ```ls``` command and if nessecery change to the Reddit_Scraper directory using ``` cd Reddit_Scraper```.

### Running the Project
1. To run this program begin by calling 
   ``` python redditScraper.py  https://old.reddit.com/r/CBRNE/](https://old.reddit.com/r/CBRNE/comments/168fbpr/which_version_of_the_jcad_can_actually_detect/ ```
      NOTE: You may use whatever thread URL you wish but the replace the "www." portion with "old."
   
2. Once you have ran this program you should see that a text file called output has been created in your directory that should have contents that resemble the output.txt avaliable for reference in this repoistory

3. Then to further extract only the comment data execute the ```extract_comments.py``` function which will create a refined version of your previous output.txt named comments.txt that should resemble the comments.txt       avaliable for reference in this repoistory



