# Vinnicius Castro
# Jan 9th 2023
import math

def vcItems():
    vc_items = int(input("Enter the number of items: "))
    return vc_items

def vcBoxes():
    vc_boxes = int(input("Enter the number of items per box: "))
    return vc_boxes
def vcCalculation(vc_n1, vc_n2):
    vc_result = math.ceil(vc_n1 / vc_n2)
    return vc_result

def vcDisplay(vc_items, vc_boxes, vc_result):
    print()
    print(f"For {vc_items} items, packing {vc_boxes} items in each box, you will need {vc_result} boxes.")

def main():
    vc_prompt1 = vcItems()
    vc_prompt2 = vcBoxes()
    vc_process = vcCalculation(vc_n1=vc_prompt1, vc_n2=vc_prompt2)
    vcDisplay(vc_items=vc_prompt1, vc_boxes= vc_prompt2, vc_result=vc_process)



if __name__ == "__main__":
    main()
    
    