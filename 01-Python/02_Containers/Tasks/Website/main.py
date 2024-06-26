# 
# ============================================================================
#Name        : main.py
#Author      : Omar Tarek Youssef
#Description : Source file for main of website task
#Date        : 26/6/2024
# ============================================================================
#

#!/usr/bin/python


import Websites 

def main():

    try:
        """
        Prints a menu of favorite websites for the user to choose from.
        """
        link = input(f"Enter your desired website from this list {Websites.favorite_websites.keys()} : ")

        if  link.strip() in Websites.favorite_websites.keys(): 
            Websites.firefox(Websites.favorite_websites[link])
        else :
            print("Please enter a valid website")

    except KeyboardInterrupt :
        print("Program terminated by user")

if __name__ == "__main__":
    main()