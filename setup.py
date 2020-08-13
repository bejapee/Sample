''' Setup script for sample project
    Run this script to start the program
'''

# Use subprocess to run an external command;
# The function 'call' works in Python 2.7;
# But in Python 3 it has been superceded by 'run'.
# Note that you must split the command line command into elements;
# That you put in a list; making sure there are no blanks.

import subprocess

print("Installing dependencies")
print
subprocess.call(["pip", "install", "-r", "requirements.txt"])
