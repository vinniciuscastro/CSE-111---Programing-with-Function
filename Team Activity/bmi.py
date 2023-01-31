from datetime import datetime
import math


def main():
    # Get the user's gender, birthdate, height, and weight.
    vc_gender = str(input("Please enter your gender (M or F): "))
    vc_bday = input("Enter your birthdate (YYYY-MM-DD): ")
    vc_weight = int(input("Enter your weight in U.S. pounds: "))
    vc_height = int(input("Enter your height in U.S. inches: "))
    # Call the compute_age, kg_from_lb, cm_from_in,
    vc_age = compute_age(vc_bday)
    vc_kg = kg_from_lb(vc_weight)
    vc_cm = cm_from_in(vc_height)
    # body_mass_index, and basal_metabolic_rate functions
    vc_bmi = body_mass_index(vc_kg, vc_cm)
    vc_bmr = basal_metabolic_rate(vc_gender,vc_kg,vc_cm,vc_age)

    

    # Print the results for the user to see.
    print(f"Age (years): {vc_age} \nWeight (kg): {vc_kg:.2f} \nHeight (cm): {vc_cm:.1f}")
    print(f"Body mass index: {vc_bmi:.1f} \nBasal metabolic rate (kcal/day): {vc_bmr:.0f}")
   


def compute_age(birth_str):
    """Compute and return a person's age in years.
    Parameter birth_str: a person's birthdate stored
        as a string in this format: YYYY-MM-DD
    Return: a person's age in years.
    """
    # Convert a person's birthdate from a string
    # to a date object.
    birthdate = datetime.strptime(birth_str, "%Y-%m-%d")
    today = datetime.now()

    # Compute the difference between today and the
    # person's birthdate in years.
    years = today.year - birthdate.year

    # If necessary, subtract one from the difference.
    if birthdate.month > today.month or \
        (birthdate.month == today.month and \
            birthdate.day > today.day):
        years -= 1

    return years


def kg_from_lb(pounds):
    """Convert a mass in pounds to kilograms.
    Parameter pounds: a mass in U.S. pounds.
    Return: the mass in kilograms.
    """
    vc_kg = pounds * 0.45359237
    return vc_kg


def cm_from_in(inches):
    """Convert a length in inches to centimeters.
    Parameter inches: a length in inches.
    Return: the length in centimeters.
    """
    vc_cm = inches * 2.54
    return vc_cm


def body_mass_index(weight, height):
    """Compute and return a person's body mass index.
    Parameters
        weight: a person's weight in kilograms.
        height: a person's height in centimeters.
    Return: a person's body mass index.
    """
    vc_bmi = 10000 * weight / height ** 2
    return vc_bmi


def basal_metabolic_rate(gender, weight, height, age):
    """Compute and return a person's basal metabolic rate.
    Parameters
        weight: a person's weight in kilograms.
        height: a person's height in centimeters.
        age: a person's age in years.
    Return: a person's basal metabolic rate in kcals per day.
    """
    if gender.upper() == "M":
        vc_bmr = 88.362 + 13.397 * weight + 4.799 * height - 5.677 * age
    elif gender.upper() == "F":
        vc_bmr = 447.593 + 9.247*weight + 3.098 * height - 4.330 * age
    else:
        vc_bmr = "Please enter gender with the same format of the example (M or F)"
    return vc_bmr


main()