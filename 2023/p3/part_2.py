import os

script_directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_directory, "input.txt")


def part_2():
    result = 0
    with open(file_path, "r") as f:
        aux_line = ["."] + list(f.readline().replace("\n", ""))
        # Artificial line for the begin
        first_line = ["."] * len(aux_line)
        second_line = aux_line
        third_line = ["."] + list(f.readline().replace("\n", ""))
        while third_line != ["."]:
            # Checking second line adjacencies
            result += gears_ratio_for_second_line(first_line, second_line, third_line)
            first_line = second_line
            second_line = third_line
            third_line = ["."] + list(f.readline().replace("\n", ""))
        third_line = ["."] * len(aux_line)
        result += gears_ratio_for_second_line(first_line, second_line, third_line)
    return result


def gears_ratio_for_second_line(
    first_line: list, second_line: list, third_line: list
) -> int:
    gear_index = total = 0
    while gear_index < len(second_line):
        # For each gear, get numbers in the lines around
        if second_line[gear_index] == "*":
            left_number_first_line, right_number_first_line = get_numbers_in_line(
                first_line, gear_index
            )
            left_number_second_line, right_number_second_line = get_numbers_in_line(
                second_line, gear_index
            )
            left_number_third_line, right_number_third_line = get_numbers_in_line(
                third_line, gear_index
            )
            all_adjacent_numbers = [
                left_number_first_line,
                right_number_first_line,
                left_number_second_line,
                right_number_second_line,
                left_number_third_line,
                right_number_third_line,
            ]
            result = 1
            if (
                all_adjacent_numbers.count(-1) == 4
            ):  # Equivalence with the condition "exactly two part numbers"
                for number in all_adjacent_numbers:
                    result *= number  # Even number of -1 has 1 as result
                total += result
        gear_index += 1
    return total


def get_numbers_in_line(line, gear_index):
    # Finding numbers in line around the index
    left = gear_index - 1
    right = gear_index + 1
    while left >= 0 and line[left].isdigit():
        left -= 1
    while right < len(line) and line[right].isdigit():
        right += 1
    list_with_numbers = line[left : right + 1]
    first_number = []
    last_number = []
    result_first = result_last = -1
    find_first = False
    # Separating found numbers
    for current_char in list_with_numbers:
        if current_char.isdigit():
            if not find_first:
                first_number.append(current_char)
            else:
                last_number.append(current_char)
        elif first_number != []:
            find_first = True
    # Casting numbers
    if first_number:
        result_first = int("".join(first_number))
    if last_number:
        result_last = int("".join(last_number))
    return result_first, result_last


if __name__ == "__main__":
    print(part_2())
