import os

script_directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_directory, "input.txt")

numbers_dict = {
    "one": 1,
    "1": 1,
    "two": 2,
    "2": 2,
    "three": 3,
    "3": 3,
    "four": 4,
    "4": 4,
    "five": 5,
    "5": 5,
    "six": 6,
    "6": 6,
    "seven": 7,
    "7": 7,
    "eight": 8,
    "8": 8,
    "nine": 9,
    "9": 9,
}


def part_1():
    total = 0
    with open(file_path, "r") as f:
        line = f.readline()
        while line:
            digits = [int(char) for char in line if char.isdigit()]
            cal_value = 10 * digits[0] + digits[-1]
            total += cal_value
            line = f.readline()
    return total


def part_2():
    total = 0
    with open(file_path, "r") as f:
        line = f.readline()
        total = 0
        while line:
            smallest = float("inf")
            gratest = -float("inf")
            first = last = 0
            for number in numbers_dict.keys():
                begin = line.find(number)
                end = line.rfind(number)
                if begin < smallest and begin != -1:
                    first = numbers_dict[number]
                    smallest = begin
                if end > gratest and end != -1:
                    last = numbers_dict[number]
                    gratest = end
            cal_value = 10 * int(first) + int(last)
            total += cal_value
            line = f.readline()
    return total


if __name__ == "__main__":
    print(part_1())
    print(part_2())
