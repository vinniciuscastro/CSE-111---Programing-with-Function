# a = 1
# b = 3
# c = -2
# result = a + b * 7 % 4 - c

# print(result)

# jan 9th 2023 class
# how to create a function
# exemple:
# def myFunction(p1,p2):
#     p = p1 + p2 
#     return p 

# input = "yes"

# while input == yes:
#     input = prompt("Do you want to continue? ");    
# def main():
#     # Get an odometer value in U.S. miles from the user.
#     start_miles = float(input(
#             "Enter the first odometer reading (miles): "))

#     # Get another odometer value in U.S. miles from the user.
#     end_miles = float(input(
#             "Enter the second odometer reading (miles): "))

#     # Get a fuel amount in U.S. gallons from the user.
#     amount_gallons = float(input(
#             "Enter the amount of fuel used (gallons): "))

#     # Call the miles_per_gallon function and store
#     # the result in a variable named mpg.
#     mpg = miles_per_gallon(start_miles, end_miles, amount_gallons)

#     # Call the lp100k_from_mpg function to convert the
#     # miles per gallon to liters per 100 kilometers and
#     # store the result in a variable named lp100k.
#     lp100k = lp100k_from_mpg(mpg)

#     # Display the results for the user to see.
#     print(f"{mpg:.1f} miles per gallon")
#     print(f"{lp100k:.2f} liters per 100 kilometers")


# def miles_per_gallon(start_miles, end_miles, amount_gallons):
#     """Compute and return the average number of miles
#     that a vehicle traveled per gallon of fuel.
#     Parameters
#         start_miles: An odometer value in miles.
#         end_miles: Another odometer value in miles.
#         amount_gallons: A fuel amount in U.S. gallons.
#     Return: Fuel efficiency in miles per gallon.
#     """
#     mpg = abs(end_miles - start_miles) / amount_gallons
#     return mpg


# def lp100k_from_mpg(mpg):
#     """Convert miles per gallon to liters per 100
#     kilometers and return the converted value.
#     Parameter mpg: A value in miles per gallon
#     Return: The converted value in liters per 100km.
#     """
#     lp100k = 235.215 / mpg
#     return lp100k


# # Call the main function so that
# # this program will start executing.
# main()

# def compute(x, y, z):
#     x = 7
#     result = compute(3, 2, x)

# for _ in range(10):
#     print("Running the loop")

# user = "Enter the percentage"
# entry = input()
# print(f"{user}: {entry}%")

# last = ["Amanda", "Fatima", "Ana Maria"]
# name = ["Silva", "Bernades", "Braga"]

# for i, iname in enumerate():
#     lastname = iname[i]
    
# Example 1

# def main():
#     # Create a dictionary with student IDs as
#     # the keys and student names as the values.
#     students = {
#         "42-039-4736": "Clint Huish",
#         "61-315-0160": "Amelia Davis",
#         "10-450-1203": "Ana Soares",
#         "75-421-2310": "Abdul Ali",
#         "07-103-5621": "Amelia Davis"
#     }

#     # Add an item to the dictionary.
#     students["81-298-9238"] = "Sama Patel"

#     # Remove an item from the dictionary.
#     students.pop("61-315-0160")

#     # Get the number of items in the dictionary.
#     length = len(students)
#     print(f"length: {length}")

#     # Print the entire dictionary.
#     print(students)
#     print()

#     # Get a student ID from the user.
#     id = input("Enter a student ID: ")

#     # Check if the student ID is in the dictionary.
#     if id in students:

#         # Find the student ID in the dictionary and
#         # retrieve the corresponding student name.
#         name = students[id]

#         # Print the student's name.
#         print(name)

#     else:
#         print("No such student")


# # Call main to start this program.
# if __name__ == "__main__":
#     main()

# Example 6

def main():
    # Create a dictionary with student IDs as the keys
    # and student data stored in a list as the values.
    students = {
        "42-039-4736": ["Clint", "Huish", "hui20001@byui.edu", 16],
        "61-315-0160": ["Amelia", "Davis", "dav21012@byui.edu", 3],
        "10-450-1203": ["Ana", "Soares", "soa22005@byui.edu", 15],
        "75-421-2310": ["Abdul", "Ali", "ali20003@byui.edu", 5],
        "07-103-5621": ["Amelia", "Davis", "dav19008@byui.edu", 0],
        "81-298-9238": ["Sama", "Patel", "pat21004@byui.edu", 8]
    }

    # These are the indexes of the elements in the value lists.
    GIVEN_NAME_INDEX = 0
    SURNAME_INDEX = 1
    EMAIL_INDEX = 2
    CREDITS_INDEX = 3

    total = 0

    # For each item in the list add the number
    # of credits that the student has earned.
    for key, value in students.items():

        # Retrieve the number of credits from the value list.
        credits = value[CREDITS_INDEX]

        # Add the number of credits to the total.
        total += credits

    print(f"Total credits earned by all students: {total}")


# Call main to start this program.
if __name__ == "__main__":
    main()