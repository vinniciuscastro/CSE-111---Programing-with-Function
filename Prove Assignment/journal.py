# Vinnicius Castro
# March 16th 2023
import csv
import random 
import datetime

def main():
    try:
        filename = "journal.txt"
        vc_main_list = []
        vc_name = get_name()
        vc_questions = questions()
        loop = True
        
        print(welcome())
        print()
        while loop:
            vc_prompt = get_choice()

            if vc_prompt == 5:
                loop = False
            elif vc_prompt == 1:
                vc_message = random.choice(vc_questions)
                print(f"\n{vc_message}")
                add_entry(vc_main_list, vc_message)
            elif vc_prompt == 2:
                print(f"\n{vc_name}, look what you have been writing:")
                print()
                display(vc_main_list)
            elif vc_prompt == 3:
                vc_main_list = load(filename)
            elif vc_prompt == 4:
                save(filename, vc_main_list)
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
def welcome():
    return "Welcome to your Journal"


def get_name():
    vc_name = input("What is your name? ")
    return vc_name

def questions():
    vc_questions = [
        "How are you feeling today?",
        "What was the best part of your day?",
        "If you had one thing you could do better today, what would it be?",
        "What are your emotions teaching you?",
        "Who do you help today, and how it felt?",
        "Who was the most interesting person you interacted with today?",
        "How did I see the hand of the Lord in my life today?",
        "What was the strongest emotion I felt today?",
    ]
    return vc_questions

def add_entry(main_list, vc_prompt):
    vc_info = {}
    vc_info["prompt"] = vc_prompt
    vc_info["content"] = input("> ")
    vc_timestamp = datetime.datetime.now()
    vc_info["timestamp"] = vc_timestamp.strftime("%m/%d/%Y")
    main_list.append(vc_info)

def display(vc_main_list):
    vc_number = 1
    for vc_entry in vc_main_list:
        print(f"{vc_number} - Date: {vc_entry['timestamp']} - Prompt: {vc_entry['prompt']}")
        print(vc_entry["content"])
        vc_number += 1 
        print()

def load(filename):
    vc_main_list = []
    with open(filename, "r") as vc_f:
        for vc_line in vc_f:
            vc_parts = vc_line.strip().split("@")
            vc_info = {"timestamp": vc_parts[0], "content": vc_parts[1], "prompt": vc_parts[2]}
            vc_main_list.append(vc_info)
    return vc_main_list


def save(filename, vc_main_list):
    with open(filename, "w") as vc_f:
        for vc_entry in vc_main_list:
            vc_line = f"{vc_entry['timestamp']}@{vc_entry['content']}@{vc_entry['prompt']}\n"
            vc_f.write(vc_line)

if __name__ == "__main__":
    main()