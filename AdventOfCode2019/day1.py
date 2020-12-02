import math

def get_input(file):
    with open(file, 'r') as f:
        in_data = []
        for data in f.readlines():
            in_data.append(int(data))
    return in_data


def calculate_fule(mas):
    fule = math.floor(mas/3) - 2 
    if fule > 0:
        return fule + calculate_fule(fule)
    else:
        return 0


def calculate_fule_list(mas_list):
    fule = 0
    for x in mas_list:
        fule += calculate_fule(x)    
    return fule


if __name__ == "__main__":
    data = get_input("day1.py")
    total_fule = calculate_fule_list(data)
    print(total_fule)

