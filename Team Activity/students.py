# Vinnicius Castro 
# Feb 27 2023

import csv

def main():
    index = 0
    name_index = 1
    students_file = read_dictionary("/Users/vinni/OneDrive/Documents/CSE 111 - Programing with Function/Team Activity/students.csv", index)

    inumber = input("Please enter an I-Number (xxxxxxxxx): ")
    inumber = inumber.replace("-", "")
    if not inumber.isdigit():
        print("Invalid character in I-Number")
    else: 
        if inumber not in students_file:
                print("No such student")
        else: 
                student = students_file[inumber]
                name = student[name_index]

                print(name)
def read_dictionary(filename, index):
    dictionary = {}

    with open(filename, "rt") as csv_file:

        reader = csv.reader(csv_file)
        next(reader)

        for row in reader:
            if len(row) != 0:
                key = row[index]
                dictionary[key] = row


    return dictionary

if __name__ == "__main__":
    main()