# Password Hash Checker

This repository contains scripts to check common passwords against hashed passwords for different users. The primary purpose is to demonstrate how common passwords can be easily cracked if they are hashed using SHA-256.

# Files in the Repository
1. commonpasswords:

This file contains a list of common passwords that are often used by individuals. Each password is on a new line.

2. username_hashes.txt:

This file contains usernames and their corresponding SHA-256 hashed passwords in the format username:hash.

3.password_check.py:

This script reads the commonpasswords file and the username_hashes.txt file, then checks if any of the common passwords match the hashed passwords for the given usernames.

4. single_password_hash.py:

This script takes a single password, hashes it using SHA-256, and prints out the resulting hash. This is useful for verifying what a specific password's hash would be.

# How to Use
## Running password_check.py

This script will compare common passwords with the hashed passwords in username_hashes.txt and print out any matches it finds.

Ensure you have commonpasswords and username_hashes.txt files in the same directory as password_check.py.

Run the script:

The script will output any matches in the format HASH FOUND\nusername:password.

## Running single_password_hash.py
This script hashes a single password using SHA-256 and prints the result.

Edit the script to change the Password variable to the password you want to hash.

Run the script:

The script will print the SHA-256 hash of the password.
