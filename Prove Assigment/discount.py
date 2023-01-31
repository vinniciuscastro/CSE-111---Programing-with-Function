# Vinnicius Castro 
# Jan 11 2023

from datetime import datetime



#get user input 
def VC_subtotal():
    vc_input = float(input("Please enter the subtotal: "))
    return vc_input

# def VC_discount():

def VC_taxes(vc_value):
    print(f"Sales tax amount: {vc_value:.2f}")

def VC_display_discount(vc_amount):
    print(f"Discount amount: {vc_amount:.2f}")

def VC_display_total(vc_total):
    print(f"Total: {vc_total:.2f}")

def main():
    vc_input = VC_subtotal()
    vc_date = datetime.now()
    vc_week = vc_date.weekday()


    if (vc_week == 2 or vc_week == 3) and vc_input > 50:
        vc_discount = vc_input * .10
        VC_display_discount(vc_discount)
        vc_sales = 0.06 * (vc_input - vc_discount) 
        VC_taxes(vc_sales)
        vc_total = (vc_input - vc_discount) + vc_sales
        VC_display_total(vc_total)
    else:
        vc_sales = vc_input * 0.06
        VC_taxes(vc_sales)
        vc_total = vc_input  + vc_sales
        VC_display_total(vc_total)

if __name__ == "__main__":
    main()

