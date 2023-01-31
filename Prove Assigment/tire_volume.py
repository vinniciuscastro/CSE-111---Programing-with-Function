#Vinnicius Castro
#Jan/07/2023

from datetime import datetime
import math

vc_w = float(input("Enter the width of the tire in mm (ex 205): "))
vc_a = float(input("Enter the aspect ratio of the tire (ex 60): "))
vc_d = float(input("Enter the diameter of the wheel in inches (ex 15): "))

vc_answer = math.pi * vc_w ** 2 * vc_a * (vc_w * vc_a + 2540 * vc_d) / 10000000000

print()

print(f"The approximate volume is {vc_answer:.2f} liters")


vc_current_date_and_time = datetime.now()
#creativity 
#days of the week 
vc_week =  vc_current_date_and_time.weekday()
if (vc_week == 0):
    vc_week = "Monday"

elif (vc_week == 1):
    vc_week = "Tuesday"
elif (vc_week == 2):
    vc_week = "Wednesday"
elif (vc_week == 3):
    vc_week = "Thursday"
elif (vc_week == 4):
    vc_week = "Friday"
elif (vc_week == 5):
    vc_week = "Saturday"
else:
    vc_week = "Sunday"



with open('volumes.txt', 'at') as vc_file:
    #I added the day of the week to the file
    vc_file.write(f"{vc_week}: {vc_current_date_and_time:%Y-%m-%d}, {vc_w:.0f}, {vc_a:.0f}, {vc_d:.0f}, {vc_answer:.2f}\n")




