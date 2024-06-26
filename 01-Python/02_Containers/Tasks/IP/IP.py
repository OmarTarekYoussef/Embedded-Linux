# 
# ============================================================================
#Name        : task2.py
#Author      : Omar Tarek Youssef
#Description : Source file for Task2 Containers
#Date        : 26/6/2024
# ============================================================================
#

#!/usr/bin/python
import requests

def ip():
    response = requests.get("https://api.ipify.org/?format=json")
    
    ip = response.json()['ip']

    response = requests.get(f"https://ipinfo.io/{ip}/geo")

    print("Country : ",response.json()['country'])
    print("Region : ",response.json()['region'])
    print("City : ",response.json()['city'])
    print("TimeZone : ",response.json()['timezone'])
        
def main():
    ip()

if __name__ == "__main__":
    main()