# 
# ============================================================================
#Name        : task2.py
#Author      : Omar Tarek Youssef
#Description : Source file for Task2 introduction to python
#Date        : 26/6/2024
# ============================================================================
#

#!/usr/bin/python

def is_vowel():
    character = input("Enter a character: ")  
    
    # Creating a list of vowels  
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']  
    if(len(character)==1):
        
        # Check if the character is a vowel or not  
        if character in vowels:  
            print(f"The character '{character}' is a vowel!")  
        else:  
            print(f"The character '{character}' is a consonant!")
    else:
        print("Please enter one character")
        is_vowel()
        
def main():
    is_vowel()

if __name__ == "__main__":
    main()