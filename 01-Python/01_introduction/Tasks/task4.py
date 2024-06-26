# 
# ============================================================================
#Name        : task4.py
#Author      : Omar Tarek Youssef
#Description : Source file for Task4 introduction to python
#Date        : 26/6/2024
# ============================================================================
#

#!/usr/bin/python

import math

def Cal_Circle_Area(radius):
    Circle_Area = (math.pi)*radius*radius
    print("Area of the circle is ",Circle_Area)
   
def main():
    Circle_radius = float(input("Enter the radius of the circle: "))
    Cal_Circle_Area(Circle_radius)
    
if __name__ == "__main__":
    main()