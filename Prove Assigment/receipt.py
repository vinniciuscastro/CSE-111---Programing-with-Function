# Vinnicius Castro 
# Feb 28th 2023
import csv
def main():
    pass

def read_dictionary(filename, key_column_index):
        # Create an empty dictionary that will
    # store the data from the CSV file.
    dictionary = {}

    # Open the CSV file for reading and store a reference
    # to the opened file in a variable named csv_file.
    with open(filename, "rt") as csv_file:


        vc_reader = csv.reader(csv_file)

        next(vc_reader)

        for vc_row_list in vc_reader:


            if len(vc_row_list) != 0:

                key = vc_row_list[key_column_index]

                dictionary[key] = vc_row_list

    # Return the dictionary.
    return dictionary


if __name__ == "__main__":
    main()
