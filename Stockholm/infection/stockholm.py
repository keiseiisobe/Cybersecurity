#! /usr/bin/python3

import argparse
import os
from os import path
import re
import cryptography

def check_if_in_home_directory():
    """
    Check if the script is running in the home directory.
    """
    home_dir = path.expanduser("~") + '/'
    current_dir = path.abspath(os.getcwd())
    if not re.match(home_dir, current_dir):
        print("Please run this script in your home directory.")
        exit(1)

def check_if_in_infection_folder():
    """
    Check if the script is running in the 'infection' folder.
    """
    current_dir = path.basename(path.abspath(os.getcwd()))
    if current_dir != "infection":
        print("Please run this script in the 'infection' folder.")
        exit(1)

if __name__ == "__main__":
    check_if_in_home_directory()
    check_if_in_infection_folder()
    parser = argparse.ArgumentParser(description="execute a harmless ransomware")
    parser.add_argument(
        "-v", "--version", action="version", version="%(prog)s 1.0" , help="show the version of the script"
    )
    parser.add_argument(
        "-r", "--reverse", dest="key", help="reverse the encryption"
    )
    parser.add_argument(
        "-s", "--silent", action="store_true", help="run in silent mode"
    )
    args = parser.parse_args()
    print(args)
    
        
