# Vinnicius Castro
# Jan 23rd 2023
import math

def main():
    vc_name = "#1 Picnic"
    vc_radius = 6.83
    vc_height = 10.16 
    vc_volume = vc_compute_volume(vc_radius, vc_height)
    vc_area = vc_compute_surface_area(vc_radius,vc_height)
    vc_result = vc_volume / vc_area
    print(f"{vc_name} {vc_result:.2f}")

    vc_name = "#1 Tall"
    vc_radius = 7.78
    vc_height = 11.91
    vc_volume = vc_compute_volume(vc_radius, vc_height)
    vc_area = vc_compute_surface_area(vc_radius,vc_height)
    vc_result = vc_volume / vc_area
    print(f"{vc_name} {vc_result:.2f}")

    vc_name = "#2"
    vc_radius = 8.73
    vc_height = 11.59	
    vc_volume = vc_compute_volume(vc_radius, vc_height)
    vc_area = vc_compute_surface_area(vc_radius,vc_height)
    vc_result = vc_volume / vc_area
    print(f"{vc_name} {vc_result:.2f}")

    vc_name = "#2.5"
    vc_radius = 10.32
    vc_height = 11.91	
    vc_volume = vc_compute_volume(vc_radius, vc_height)
    vc_area = vc_compute_surface_area(vc_radius,vc_height)
    vc_result = vc_volume / vc_area
    print(f"{vc_name} {vc_result:.2f}")

    vc_name = "#3 Cylinder"
    vc_radius = 10.79
    vc_height = 17.78	
    vc_volume = vc_compute_volume(vc_radius, vc_height)
    vc_area = vc_compute_surface_area(vc_radius,vc_height)
    vc_result = vc_volume / vc_area
    print(f"{vc_name} {vc_result:.2f}")

    vc_name = "#5"
    vc_radius = 13.02	
    vc_height = 14.29	
    vc_volume = vc_compute_volume(vc_radius, vc_height)
    vc_area = vc_compute_surface_area(vc_radius,vc_height)
    vc_result = vc_volume / vc_area
    print(f"{vc_name} {vc_result:.2f}")

    vc_name = "#6Z"
    vc_radius = 5.40
    vc_height = 8.89	
    vc_volume = vc_compute_volume(vc_radius, vc_height)
    vc_area = vc_compute_surface_area(vc_radius,vc_height)
    vc_result = vc_volume / vc_area
    print(f"{vc_name} {vc_result:.2f}")

    vc_name = "#8Z short"
    vc_radius = 6.83
    vc_height = 7.62
    vc_volume = vc_compute_volume(vc_radius, vc_height)
    vc_area = vc_compute_surface_area(vc_radius,vc_height)
    vc_result = vc_volume / vc_area
    print(f"{vc_name} {vc_result:.2f}")

    vc_name = "#10"
    vc_radius = 15.72	
    vc_height = 17.78		
    vc_volume = vc_compute_volume(vc_radius, vc_height)
    vc_area = vc_compute_surface_area(vc_radius,vc_height)
    vc_result = vc_volume / vc_area
    print(f"{vc_name} {vc_result:.2f}")

    vc_name = "#211"
    vc_radius = 6.83	
    vc_height = 12.38
    vc_volume = vc_compute_volume(vc_radius, vc_height)
    vc_area = vc_compute_surface_area(vc_radius,vc_height)
    vc_result = vc_volume / vc_area
    print(f"{vc_name} {vc_result:.2f}")

    vc_name = "#300"
    vc_radius = 7.62
    vc_height = 11.27
    vc_volume = vc_compute_volume(vc_radius, vc_height)
    vc_area = vc_compute_surface_area(vc_radius,vc_height)
    vc_result = vc_volume / vc_area
    print(f"{vc_name} {vc_result:.2f}")

    vc_name = "#303"
    vc_radius = 8.10
    vc_height = 11.11	
    vc_volume = vc_compute_volume(vc_radius, vc_height)
    vc_area = vc_compute_surface_area(vc_radius,vc_height)
    vc_result = vc_volume / vc_area
    print(f"{vc_name} {vc_result:.2f}")

    print()
    vc_lists = [
        ["#1 Picnic",6.83, 10.16],
        ["#1 Tall", 7.78, 11.91],
        ["#2", 8.73, 11.59,],
        ["#2.5", 10.32, 11.91],
        ["#3 Cylinder", 10.79, 17.78],
        ["#5", 13.02, 14.29],
        ["#6Z", 5.40, 8.89],
        ["#8Z short", 6.83, 7.62],
        ["#10", 15.72, 17.78],
        ["#211", 6.83, 12.38],
        ["#300", 7.62, 11.27],
        ["#303", 8.10, 11.11]
    ]

    for vc_list in vc_lists:
        vc_name = vc_list[0]
        vc_radius = vc_list[1]
        vc_height = vc_list[2]
        vc_volume = vc_compute_volume(vc_radius, vc_height)
        vc_area = vc_compute_surface_area(vc_radius,vc_height)
        vc_result = vc_volume / vc_area
        print(f"{vc_name} {vc_result:.2f}")


def vc_compute_volume(vc_radius, vc_height):
    vc_volume = math.pi * vc_radius ** 2 * vc_height
    return vc_volume


def vc_compute_surface_area(vc_radius, vc_height):
    vc_result = 2 * math.pi * vc_radius * (vc_radius + vc_height)
    return vc_result

main()