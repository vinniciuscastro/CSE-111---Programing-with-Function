# Example 1

# def main():
#     # Read the contents of a text file
#     # named plants.txt into a list.
#     text_list = read_list("plants.txt")

#     # Print the entire list.
#     print(text_list)


# def read_list(filename):
#     """Read the contents of a text file into a list and
#     return the list. Each element in the list will contain
#     one line of text from the text file.

#     Parameter filename: the name of the text file to read
#     Return: a list of strings
#     """
#     # Create an empty list that will store
#     # the lines of text from the text file.
#     text_list = []

#     # Open the text file for reading and store a reference
#     # to the opened file in a variable named text_file.
#     with open(filename, "rt") as text_file:

#         # Read the contents of the text
#         # file one line at a time.
#         for line in text_file:

#             # Remove white space, if there is any,
#             # from the beginning and end of the line.
#             clean_line = line.strip()

#             # Append the clean line of text
#             # onto the end of the list.
#             text_list.append(clean_line)

#     # Return the list that contains the lines of text.
#     return text_list


# # Call main to start this program.
# if __name__ == "__main__":
#     main()

# Example 2

# import csv

# def main():
#     # Open the CSV file for reading and store a reference
#     # to the opened file in a variable named csv_file.
#     with open("hymns.csv", "rt") as csv_file:

#         # Use the csv module to create a reader object
#         # that will read from the opened CSV file.
#         reader = csv.reader(csv_file)

#         # Read the rows in the CSV file one row at a time.
#         # The reader object returns each row as a list.
#         for row_list in reader:
#             print(row_list)


# # Call main to start this program.
# if __name__ == "__main__":
#     main()

# Example 3

# import csv

# # Indexes of some of the columns
# # in the dentists.csv file.
# COMPANY_NAME_INDEX = 0
# NUM_EMPS_INDEX = 3
# NUM_PATIENTS_INDEX = 4


# def main():
#     # Open a file named dentists.csv and store a reference
#     # to the opened file in a variable named dentists_file.
#     with open("dentists.csv", "rt") as dentists_file:

#         # Use the csv module to create a reader
#         # object that will read from the opened file.
#         reader = csv.reader(dentists_file)

#         # The first row of the CSV file contains column
#         # headings and not data about a dental office,
#         # so this statement skips the first row of the
#         # CSV file.
#         next(reader)

#         running_max = 0
#         most_office = None

#         # Read each row in the CSV file one at a time.
#         # The reader object returns each row as a list.
#         for row_list in reader:

#             # For the current row, retrieve the
#             # values in columns 0, 3, and 4.
#             company = row_list[COMPANY_NAME_INDEX]
#             num_employees = int(row_list[NUM_EMPS_INDEX])
#             num_patients = int(row_list[NUM_PATIENTS_INDEX])

#             # Compute the number of patients per
#             # employee for the current dental office.
#             patients_per_emp = num_patients / num_employees

#             # If the current dental office has more
#             # patients per employee than the running
#             # maximum, assign running_max and most_office
#             # to be the current dental office.
#             if patients_per_emp > running_max:
#                 running_max = patients_per_emp
#                 most_office = company

#     # Print the results for the user to see.
#     print(f"{most_office} has {running_max:.1f}"
#             " patients per employee")


# # Call main to start this program.
# if __name__ == "__main__":
#     main()

# Example 5

# import csv


# def main():
#     # Index of the phone number column
#     # in the dentists.csv file.
#     PHONE_INDEX = 2

#     # Read the contents of the dentists.csv into a
#     # compound dictionary named dentists_dict. Use
#     # the phone numbers as the keys in the dictionary.
#     dentists_dict = read_dictionary("dentists.csv", PHONE_INDEX)

#     # Print the dentists compound dictionary.
#     print(dentists_dict)


# def read_dictionary(filename, key_column_index):
#     """Read the contents of a CSV file into a compound
#     dictionary and return the dictionary.

#     Parameters
#         filename: the name of the CSV file to read.
#         key_column_index: the index of the column
#             to use as the keys in the dictionary.
#     Return: a compound dictionary that contains
#         the contents of the CSV file.
#     """
#     # Create an empty dictionary that will
#     # store the data from the CSV file.
#     dictionary = {}

#     # Open the CSV file for reading and store a reference
#     # to the opened file in a variable named csv_file.
#     with open(filename, "rt") as csv_file:

#         # Use the csv module to create a reader object
#         # that will read from the opened CSV file.
#         reader = csv.reader(csv_file)

#         # The first row of the CSV file contains column
#         # headings and not data, so this statement skips
#         # the first row of the CSV file.
#         next(reader)

#         # Read the rows in the CSV file one row at a time.
#         # The reader object returns each row as a list.
#         for row_list in reader:

#             # If the current row is not blank, add the
#             # data from the current to the dictionary.
#             if len(row_list) != 0:

#                 # From the current row, retrieve the data
#                 # from the column that contains the key.
#                 key = row_list[key_column_index]

#                 # Store the data from the current
#                 # row into the dictionary.
#                 dictionary[key] = row_list

#     # Return the dictionary.
#     return dictionary


# # Call main to start this program.
# if __name__ == "__main__":
#     main()

# def askUserforIntenger():
#     flag= True
#     while (flag):
#         try:
#             str_value = input("Enter a Whole Number")
#             value = int(str_value)
#             flag = false
#         except ValueError:
#             print("Please enter a whole number")
# ---------------------------------------------------------------------------
# def main():
#     fahr_temps = [72, 65, 71, 75, 82, 87, 68]

#     # Print the Fahrenheit temperatures.
#     print(f"Fahrenheit: {fahr_temps}")

#     # Convert each Fahrenheit temperature to Celsius and store
#     # the Celsius temperatures in a list named cels_temps.
#     cels_temps = []
#     for fahr in fahr_temps:
#         cels = cels_from_fahr(fahr)
#         cels_temps.append(cels)

#     # Print the Celsius temperatures.
#     print(f"Celsius: {cels_temps}")


# def cels_from_fahr(fahr):
#     """Convert a Fahrenheit temperature to
#     Celsius and return the Celsius temperature.
#     """
#     cels = (fahr - 32) * 5 / 9
#     return round(cels, 1)


# # Call main to start this program.
# if __name__ == "__main__":
#     main()

# def main():
#     fahr_temps = [72, 65, 71, 75, 82, 87, 68]

#     # Print the Fahrenheit temperatures.
#     print(f"Fahrenheit: {fahr_temps}")

#     # Convert each Fahrenheit temperature to Celsius and store
#     # the Celsius temperatures in a list named cels_temps.
#     cels_temps = list(map(cels_from_fahr, fahr_temps))

#     # Print the Celsius temperatures.
#     print(f"Celsius: {cels_temps}")


# def cels_from_fahr(fahr):
#     """Convert a Fahrenheit temperature to
#     Celsius and return the Celsius temperature.
#     """
#     cels = (fahr - 32) * 5 / 9
#     return round(cels, 1)


# # Call main to start this program.
# if __name__ == "__main__":
#     main()
# ---------------------------------------------------------------------------
# Example 3
# Nested Functions

# def main():

#     def cels_from_fahr(fahr):
#         """Convert a Fahrenheit temperature to
#         Celsius and return the Celsius temperature.
#         """
#         cels = (fahr - 32) * 5 / 9
#         return round(cels, 1)

#     fahr_temps = [72, 65, 71, 75, 82, 87, 68]

#     # Print the Fahrenheit temperatures.
#     print(f"Fahrenheit: {fahr_temps}")

#     # Convert each Fahrenheit temperature to Celsius and store
#     # the Celsius temperatures in a list named cels_temps.
#     cels_temps = list(map(cels_from_fahr, fahr_temps))

#     # Print the Celsius temperatures.
#     print(f"Celsius: {cels_temps}")


# # Call main to start this program.
# if __name__ == "__main__":
#     main()
# ---------------------------------------------------------------------------
# Example 4
# Lambda Functions

# def main():
#     fahr_temps = [72, 65, 71, 75, 82, 87, 68]

#     # Print the Fahrenheit temperatures.
#     print(f"Fahrenheit: {fahr_temps}")

#     # Define a lambda function that converts
#     # a Fahrenheit temperature to Celsius and
#     # returns the Celsius temperature.
#     cels_from_fahr = lambda fahr: round((fahr - 32) * 5 / 9, 1)

#     # Convert each Fahrenheit temperature to Celsius and store
#     # the Celsius temperatures in a list named cels_temps.
#     cels_temps = list(map(cels_from_fahr, fahr_temps))

#     # Print the Celsius temperatures.
#     print(f"Celsius: {cels_temps}")


# # Call main to start this program.
# if __name__ == "__main__":
#     main()
# ---------------------------------------------------------------------------
# Example 5
# Example - Map and Filter

# def main():
#     # Read a file that contains a list
#     # of Canadian province names.
#     provinces_list = read_list("provinces.txt")

#     # As a debugging aid, print the entire list.
#     print("Original list of provinces:")
#     print(provinces_list)
#     print()

#     # Define a nested function that converts AB to Alberta.
#     def alberta_from_ab(province_name):
#         if province_name == "AB":
#             province_name = "Alberta"
#         return province_name

#     # Replace all occurrences of "AB" with "Alberta" by
#     # calling the map function and passing the ablerta_from_ab
#     # function and provinces_list into the map function.
#     new_list = list(map(alberta_from_ab, provinces_list))
#     print("List of provinces after AB was changed to Alberta:")
#     print(new_list)
#     print()

#     # Define a lambda function that returns True if a
#     # province's name is Alberta and returns False otherwise.
#     is_alberta = lambda name: name == "Alberta"

#     # Filter the new list to only those provinces that
#     # are "Alberta" by calling the filter function and
#     # passing the is_alberta function and new_list.
#     filtered_list = list(filter(is_alberta, new_list))
#     print("List filtered to Alberta only:")
#     print(filtered_list)
#     print()

#     # Because all the elements in filtered_list are
#     # "Alberta", we can count how many elements are
#     # "Alberta" by simply calling the len function.
#     count = len(filtered_list)

#     print(f"Alberta occurs {count} times in the modified list.")


# # Call main to start this program.
# if __name__ == "__main__":
#     main()
# ---------------------------------------------------------------------------
# Example 6
# Sorting a Compound List

# def main():
#     # Create a list that contains country names
#     # and print the list.
#     countries = [
#         "Canada", "France", "Ghana", "Brazil", "Japan"
#     ]
#     print(countries)

#     # Sort the list. Then print the sorted list.
#     sorted_list = sorted(countries)
#     print(sorted_list)


# # Call main to start this program.
# if __name__ == "__main__":
#     main()
# ---------------------------------------------------------------------------
# Example 7
# Sorting a Compound List
# def main():
#     # Create a list that contains data about countries.
#     countries = [
#         # [country_name, land_area, population, gdp_per_capita]
#         ["Mexico", 1972550, 126014024, 21362],
#         ["France",  640679,  67399000, 45454],
#         ["Ghana",   239567,  31072940,  7343],
#         ["Brazil", 8515767, 210147125, 14563],
#         ["Japan",   377975, 125480000, 41634]
#     ]

#     # Print the unsorted list.
#     print("Original unsorted list of countries")
#     for country in countries:
#         print(country)
#     print()

#     # Define a lambda function that will be used as the
#     # key function by the sorted function. The lambda
#     # function extracts the population data from a
#     # country so that the population will be used for
#     # sorting the list of countries.
#     POPULATION_INDEX = 2
#     popul_func = lambda country: country[POPULATION_INDEX]

#     # Sort the list of countries by the population.
#     sorted_list = sorted(countries, key=popul_func)

#     # Print the sorted list.
#     print("List of countries sorted by population")
#     for country in sorted_list:
#         print(country)


# # Call main to start this program.
# if __name__ == "__main__":
#     main()

# Example 8
# Sorting a Compound List
def main():
    # Create a list that contains data about young students.
    students = [
        # [given_name, surname, reading_level]
        ["Robert", "Smith", 6.7],
        ["Annie", "Smith", 6.2],
        ["Robert", "Lopez", 7.1],
        ["Sean", "Li", 5.6],
        ["Sofia", "Lopez", 5.3],
        ["Lily", "Harris", 6.7],
        ["Alex", "Harris", 5.8]
    ]

    GIVEN_INDEX = 0
    SURNAME_INDEX = 1

    # Define a lambda function that combines
    # a student's surname and given name.
    combine_names = lambda student_list: \
        f"{student_list[SURNAME_INDEX]}, {student_list[GIVEN_INDEX]}"

    # Sort the list by the combined key of surname, given_name.
    sorted_list = sorted(students, key=combine_names)

    # Print the list.
    for student in sorted_list:
        print(student)


# Call main to start this program.
if __name__ == "__main__":
    main()