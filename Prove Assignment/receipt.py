# Vinnicius Castro 
# Feb 28th 2023
import csv
from datetime import datetime
def main():
    try:
        vc_index = 0
        product_name = 0
        requested_quantity = 1
        product_price = 2
        sales_rate = 6
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
        vc_items = number_of_items(requested_quantity)
        vc_subtotal = subtotal(product_price,product_dic, product_name, requested_quantity)
        vc_sale_tax = sales_tax(vc_subtotal, sales_rate)
        vc_total = total(vc_sale_tax, vc_subtotal)
        vc_discount = discount(vc_total)
        print()
        vc_register = input("Would you like to create an account and get 10% of discount of the total price(type: yes or no)? ")
        print()
        if vc_register.lower() == 'yes': 
            vc_namef = input("Please enter your first name: ")
            vc_namel = input("Please enter your last name: ")
            vc_email = input("Please enter a valid email: ")
            print("\n*******************************************")
            print(f"{vc_namef.capitalize()} {vc_namel.capitalize()}Thank you for creating an account! \nThe confirmation will be send to {vc_email}")
            print("*******************************************")
            print()
            print(f"Number of Items: {vc_items}")
            print(f"Subtotal: {vc_subtotal:.2f}")
            print(f"Sales Tax: {vc_sale_tax:.2f}")
            print(f"Total: {vc_total:.2f}")
            print(f"Discount: {vc_total - vc_discount:.2f}")
            print(f"Total with discount: {vc_discount:.2f}")
        else:
            print(f"Number of Items: {vc_items}")
            print(f"Subtotal: {vc_subtotal:.2f}")
            print(f"Sales Tax: {vc_sale_tax:.2f}")
            print(f"Total: {vc_total:.2f}")
        print()
        print("Thank you for shopping at the Inkom Emporium.")
        current_date_and_time = datetime.now()
        print(f"{current_date_and_time:%A %I:%M %p}")

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
def number_of_items(requested_quantity):
    vc_request_list = []
    with open("/Users/vinni/OneDrive/Documents/CSE 111 - Programing with Function/Prove Assignment/request.csv", "rt") as vc_requests:
        vc_reader = csv.reader(vc_requests)
        next(vc_reader)
        for row in vc_reader:
            vc_quantity = int(row[requested_quantity])
            vc_request_list.append(vc_quantity)
        return sum(vc_request_list)
def subtotal(product_price,product_dic, product_name, requested_quantity):
    vc_request_list = []
    vc_subtotal = 1.0
    with open("/Users/vinni/OneDrive/Documents/CSE 111 - Programing with Function/Prove Assignment/request.csv", "rt") as vc_requests:
        vc_reader = csv.reader(vc_requests)
        next(vc_reader)

        for row in vc_reader:
            vc_product_name = row[product_name]
            vc_quantity = int(row[requested_quantity])
            vc_price = float(product_dic[vc_product_name][product_price])
            vc_request_list.append([vc_quantity, vc_price])
            vc_subtotal = 0.0
            for vc_item in vc_request_list:
                vc_subtotal += vc_item[0] * vc_item[1]
        return vc_subtotal

def sales_tax(vc_subtotal, sales_tax):
    vc_sales_tax = float(vc_subtotal * (sales_tax / 100))
    return vc_sales_tax

def total(vc_sales_tax, vc_subtotal):
    vc_total = vc_sales_tax + vc_subtotal
    return vc_total

def discount(vc_total):
    vc_discount = vc_total * 0.1 
    vc_discounted_price = vc_total - vc_discount 
    return vc_discounted_price

if __name__ == "__main__":
    main()
