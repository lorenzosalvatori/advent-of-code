# https://adventofcode.com/2024/day/3

def main():
    result = 0

    with open("2024/day3/day3.input", "r") as f:
        f = f.read()

    next_useful_index = 0
    
    for i in range(len(f)):
        if i < next_useful_index:
            continue
        first_number = ""
        second_number = ""
        if f[i:i+3] == "mul":
            if f[i+3] == '(':
                first_num_index = i+4
                while f[first_num_index].isdigit():
                    first_number += f[first_num_index]
                    first_num_index += 1
                if first_number != "":
                    if f[first_num_index] == ',':
                        second_num_index = first_num_index
                        second_num_index += 1
                        while f[second_num_index].isdigit():
                            second_number += f[second_num_index]
                            second_num_index += 1
                        if second_number != "":
                            if f[second_num_index] == ')':
                                result += int(first_number)*int(second_number)
                                next_useful_index = second_num_index+1

    return result

if __name__ == "__main__":
    print(main())