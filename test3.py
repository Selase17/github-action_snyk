import os

# Get user input for a file list
filename = input("Enter the filename to list: ")

# Vulnerable to command injection if user input is not sanitized
os.system(f"ls -l {filename}")