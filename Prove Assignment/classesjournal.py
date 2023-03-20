# Vinnicius Castro
# March 16th 2023
import random
import datetime


def load(filename):
    main_list = []
    with open(filename, "r") as f:
        for line in f:
            parts = line.strip().split("@")
            info = {"timestamp": parts[0], "content": parts[1], "prompt": parts[2]}
            main_list.append(info)
    return main_list


def save(filename, main_list):
    with open(filename, "w") as f:
        for entry in main_list:
            line = f"{entry['timestamp']}@{entry['content']}@{entry['prompt']}\n"
            f.write(line)


def add_entry(main_list, prompt):
    info = {}
    info["prompt"] = prompt
    info["content"] = input("> ")
    timestamp = datetime.datetime.now()
    info["timestamp"] = timestamp.strftime("%m/%d/%Y")
    main_list.append(info)


def display(main_list):
    for entry in main_list:
        print(f"Date: {entry['timestamp']} - Prompt: {entry['prompt']}")
        print(entry["content"])
        print("")


def get_name():
    name = input("What is your name? ")
    return name


def get_menu():
    menu = [
        "How are you feeling today?",
        "What was the best part of your day?",
        "If you had one thing you could do better today, what would it be?",
        "What are your emotions teaching you?",
        "Who do you help today, and how it felt?",
        "Who was the most interesting person you interacted with today?",
        "How did I see the hand of the Lord in my life today?",
        "What was the strongest emotion I felt today?",
    ]
    return menu


def get_choice():
    print("Please select one of the following choices:")
    print("1. Write")
    print("2. Display")
    print("3. Load")
    print("4. Save")
    print("5. Quit")
    prompt = input("What would you like to do? ")
    return prompt


def main():
    filename = "journal.txt"
    main_list = []
    menu = get_menu()
    name = get_name()
    loop = True

    while loop:
        prompt = get_choice()

        if prompt == "5":
            loop = False
        elif prompt == "1":
            promptMessage = random.choice(menu)
            print(promptMessage)
            add_entry(main_list, promptMessage)
        elif prompt == "2":
            print(f"{name}, look what you have been writing:")
            print("")
            display(main_list)
        elif prompt == "3":
            main_list = load(filename)
        elif prompt == "4":
            save(filename, main_list)
        else:
            print("Choice not valid, please try again.")


if __name__ == "__main__":
    main()