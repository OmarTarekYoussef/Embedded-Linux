# 
# ============================================================================
#Name        : Websites.py
#Author      : Omar Tarek Youssef
#Description : Source file for fav websites 
#Date        : 26/6/2024
# ============================================================================
#

#!/usr/bin/python

import webbrowser

# List of favorite websites
favorite_websites = {
    'Google'        : 'https://www.google.com',
    'YouTube'       : 'https://www.youtube.com',
    'GitHub'        : 'https://www.github.com',
    'Stack Overflow': 'https://stackoverflow.com',
    'Facebook'      : 'https://www.facebook.com/',
    'Instagram'     : 'https://www.instagram.com/',
    'Linkedin'      : 'https://www.linkedin.com/'
}

def firefox(url):
    """
    Opens the given URL in the default web browser.
    """
    webbrowser.open(url)
    