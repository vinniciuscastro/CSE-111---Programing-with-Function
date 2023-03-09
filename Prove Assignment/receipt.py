# Vinnicius Castro 
# Feb 28th 2023
import csv
def main():
    try:
        vc_index = 0
        product_name = 0
        requested_quantity = 1
        product_price = 2
        filename = "/Users/vinni/OneDrive/Documents/CSE 111 - Programing with Function/Prove Assignment/products.csv"
        product_dic = read_dictionary(filename,vc_index)
        # print(f"All Products\n{product_dic}")
        print("Inkom Emporium")
        print("")
        vc_request = get_request(product_name, requested_quantity, product_dic, product_price)
        for vc_i in vc_request: 
            vc_product_num = vc_i[vc_index]
            vc_quantity = vc_i[requested_quantity]
            vc_price = vc_i[product_price]
            print(f'{vc_product_num} {vc_quantity} @ {vc_price}')
 
    except FileNotFoundError as not_found_err:
        # This code will be executed if the user enters
        # the name of a file that doesn't exist.
        print()
        print(type(not_found_err).__name__, not_found_err, sep=": ")
        print(f"The file {filename} doesn't exist.")
        print("Run the program again and enter the" \
                " name of an existing file.")

    except PermissionError as perm_err:
        # This code will be executed if the user enters the name
        # of a file and doesn't have permission to read that file.
        print()
        print(type(perm_err).__name__, perm_err, sep=": ")
        print(f"You don't have permission to read {filename}.")
        print("Run the program again and enter the name" \
                " of a file that you are allowed to read.")

    except ValueError as val_err:
        # This code will be executed if the user enters
        # an invalid integer for the line number.
        print()
        print(type(val_err).__name__, val_err, sep=": ")
        print("You entered an invalid integer for the line number.")
        print("Run the program again and enter an integer for" \
                " the line number.")

    # except IndexError as index_err:
    #     # This code will be executed if the user enters a valid
    #     # integer for the line number, but the integer is greater
    #     # than the number of lines in the file.
    #     print()
    #     print(type(index_err).__name__, index_err, sep=": ")
    #     length = len(text_lines)
    #     if linenum < 0:
    #         print(f"{linenum} is a negative integer.")
    #     else:
    #         print(f"{linenum} is greater than the number" \
    #                 f" of lines in {filename}.")
    #         print(f"There are only {length} lines in {filename}.")
    #     print(f"Run the program again and enter a line number" \
    #             f" between 1 and {length}.")

    except Exception as excep:
        # This code will be executed if some
        # other type of exception occurs.
        print()
        print(type(excep).__name__, excep, sep=": ")
            




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

def get_request(product_name, requested_quantity, product_dic, product_price):
    vc_request_list = []
    with open("/Users/vinni/OneDrive/Documents/CSE 111 - Programing with Function/Prove Assignment/request.csv", "rt") as vc_requests:
        vc_reader = csv.reader(vc_requests)
        next(vc_reader)

        for row in vc_reader:
            vc_product_name = row[product_name]
            vc_quantity = int(row[requested_quantity])
            vc_name = product_dic[vc_product_name][1]
            vc_price = float(product_dic[vc_product_name][product_price])
            
            vc_request_list.append([vc_name,vc_quantity, vc_price])
            
        return vc_request_list


if __name__ == "__main__":
    main()
