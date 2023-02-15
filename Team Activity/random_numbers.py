# Vinnicius Castro
# Feb 14th 2023
import random 
def main():
    numbers = [16.2, 75.1, 52.3]
    print("Before:")
    append_random_numbers(numbers,)
    print("After:")
    append_random_numbers(numbers, 2)

def append_random_numbers(numbers_list, quantity=1):
    vc_n = random.uniform(1, 100)
    vc_rn = round(vc_n,1)
    for vc_i in range(quantity):
        numbers_list.append(vc_rn)
        print(f"numbers {numbers_list}")




if __name__ == "__main__":
    main()