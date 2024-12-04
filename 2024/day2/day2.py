# https://adventofcode.com/2024/day/2

def main():
    safe_reports = 0
    with open("2024/day2/day2.input", "r") as f:
        for line in f.readlines():
            levels_list = line.split()
            levels_list = [int(n) for n in levels_list]
            sorted_list = sorted(levels_list)
            if levels_list == sorted_list or levels_list == sorted_list[::-1]:
                for i in range(len(levels_list)):
                    if i < len(levels_list)-1:
                        if abs(levels_list[i] - levels_list[i+1]) > 3 or levels_list[i] == levels_list[i+1]:
                            break
                else:
                    safe_reports += 1

    return safe_reports

if __name__ == "__main__":
    print(main())