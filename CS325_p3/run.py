# This file is a rudientary directory change to access the functionality of all of the subfolders of CS325_p3


import os
import subprocess

# Change the current working directory to Module_1
module1_dir = 'Module_1'
os.chdir(module1_dir)

# Run main.py in Module_1
subprocess.run(['python', 'main.py'])






