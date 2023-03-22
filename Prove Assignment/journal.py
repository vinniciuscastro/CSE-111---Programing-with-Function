# Vinnicius Castro
# March 16th 2023
import csv
import random 
from datetime import datetime

def main():
    try:
        vc_main_list = []
        vc_name = get_name()
        loop = True

        while loop:
            vc_prompt = get_choice()

            if vc_prompt == 5:
                loop = False
            else:
                print("Choice not valid, please try again.")

    except (FileNotFoundError, PermissionError) as error:
        print(error)
        print("Please choose a different file.")

    except ValueError as val_err:
        print("Error:", val_err)
    except ZeroDivisionError:
        print("Cannot divide by zero.")

def get_choice():
    print("Please select one of the following choices:")
    print("1. Write")
    print("2. Display")
    print("3. Load")
    print("4. Save")
    print("5. Quit")
    vc_prompt = int(input("What would you like to do? "))
    return vc_prompt

def get_name():
    vc_name = input("What is your name? ")
    return vc_name

def date():
    vc_current_date_and_time = datetime.now()
    
    

if __name__ == "__main__":
    main()