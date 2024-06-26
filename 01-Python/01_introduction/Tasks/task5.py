# 
# ============================================================================
#Name        : task5.py
#Author      : Omar Tarek Youssef
#Description : Source file for Task5 introduction to python
#Date        : 26/6/2024
# ============================================================================
#

#!/usr/bin/python

import calendar 


year = int(input("Enter the year: ")) 
month = int(input("Enter the month (1-12): ")) 

def Cal(year, month):
    cal = calendar.month(year, month) 
    print("Calendar for {}-{}".format(year, month)) 
    print(cal) 
   
def main():
    Cal(year, month)
    
if __name__ == "__main__":
    main()