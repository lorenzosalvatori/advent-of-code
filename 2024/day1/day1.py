# https://adventofcode.com/2024/day/1

def main():
    distance = 0
    with open("2024/day1/day1.input", "r") as f:
        left_list = []
        right_list = []

        for line in f.readlines():
            numbers = line.split()
            left_list.append(int(numbers[0]))
            right_list.append(int(numbers[-1]))

    left_list.sort()
    right_list.sort()

    for i in range(len(left_list)):
        distance += abs(left_list[i] - right_list[i])

    return distance

if __name__ == "__main__":
    print(main())