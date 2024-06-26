# 
# ============================================================================
#Name        : task3.py
#Author      : Omar Tarek Youssef
#Description : Source file for Task3 introduction to python
#Date        : 26/6/2024
# ============================================================================
#

#!/usr/bin/python

import os

def get_environment_variable(env_variable_name):
    return os.environ.get(env_variable_name)
   
def main():
    
    env_variable= 'PATH'
    path_value = get_environment_variable(env_variable)
    print(f"The value of the {env_variable} environment variable is: {path_value}")

if __name__ == "__main__":
    main()