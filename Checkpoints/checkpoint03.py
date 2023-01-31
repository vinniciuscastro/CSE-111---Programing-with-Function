# Vinnicius Castro 
# Jan 17th 2023

def main():
    vc_beginning = float(input("Enter the first odometer reading (miles): "))
    vc_end = float(input("Enter the second odometer reading (miles): "))
    #miles per gallons 
    vc_mpg = float(input("Enter the amount of fuel used (gallons): "))
    vc_mpg_result = vc_miles_per_gallon(vc_beginning,vc_end, vc_mpg)
    vc_lpk_result = vc_lp100k_from_mpg(vc_mpg_result)
    print(f"{vc_mpg_result:.1f} miles per gallon\n{vc_lpk_result:.2f} liters per 100 kilometers")
    


def vc_miles_per_gallon(vc_start_miles, vc_end_miles, vc_amount_gallons):
    vc_result = abs(vc_end_miles - vc_start_miles) / vc_amount_gallons
    return vc_result


def vc_lp100k_from_mpg(vc_mpg_input):
    vc_lp100k = 235.215 / vc_mpg_input
    return vc_lp100k


# Call the main function so that
# this program will start executing.
main()