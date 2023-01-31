#Vinnicius Castro
#Jan/04/2023

#all variables have to start with my initials (vc)


vc_user = int(input("Please enter your age: "))

vc_heartbeats = 220 - vc_user

vc_hmin = int(vc_heartbeats*0.65)
vc_hmax = int(vc_heartbeats*0.85)


print(f"When you exercise to strengthen your heart, you should\nkeep your heart rate between {vc_hmin} and {vc_hmax} \nbeats per minute.")