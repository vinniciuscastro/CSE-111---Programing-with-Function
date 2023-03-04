# Vinnicius Castro 
# Feb 28th 2023
import csv
def main():
    vc_index = 0
    product_name = 0
    requested_quantity = 1
    product_price = 2
    product_dic = read_dictionary("/Users/vinni/OneDrive/Documents/CSE 111 - Programing with Function/Prove Assignment/products.csv",vc_index)
    print(f"All Products\n{product_dic}")
    print()
    print("Requested Items")

    with open("/Users/vinni/OneDrive/Documents/CSE 111 - Programing with Function/Prove Assignment/request.csv", "rt") as vc_requests:
        vc_reader = csv.reader(vc_requests)
        next(vc_reader)

        for row in vc_reader:
            vc_product_name = row[product_name]
            
            vc_quantity = int(row[requested_quantity])
            vc_name = product_dic[vc_product_name][1]
            vc_individual_price = float(product_dic[vc_product_name][product_price])
            vc_price = vc_quantity * vc_individual_price
            print(f"{vc_name}: {vc_quantity} @ {vc_individual_price:.2f}")

            # if vc_product_name not in product_dic:
            #     print("No such product")
            




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
