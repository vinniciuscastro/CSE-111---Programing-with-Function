
def main():
    provinces = read_file("/Users/vinni/OneDrive/Documents/CSE 111 - Programing with Function/Checkpoints/provinces.txt")
    print(provinces) 
    provinces.pop(0) 
    provinces.pop()  
    for i in range(len(provinces)):
        if provinces[i] == "AB":
            provinces[i] == "Alberta"
    number = provinces.count("Alberta")

    print(f"\n Alberta occurs {number} times in the modified list.")
def read_file(filename):
    text_list = []
    with open(filename, "rt") as text_file:
        for line in text_file:
            clean_line = line.strip()
            text_list.append(clean_line)

    return text_list


if __name__ == "__main__":
    main()