import os

script_directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_directory, "input.txt")


def part_1():
    result = 0
    with open(file_path, "r") as f:
        aux_line = ["."] + list(f.readline().replace("\n", ""))
        # Artificial line for the begin
        first_line = ["."] * len(aux_line)
        second_line = aux_line
        third_line = ["."] + list(f.readline().replace("\n", ""))
        while third_line != ["."]:
            # Checking second line adjacencies
            result += check_engine_line(first_line, second_line, third_line)
            first_line = second_line
            second_line = third_line
            third_line = ["."] + list(f.readline().replace("\n", ""))
        third_line = ["."] * len(aux_line)
        result += check_engine_line(
            list(first_line), list(second_line), list(third_line)
        )
    return result


def check_engine_line(first_line: list, second_line: list, third_line: list) -> int:
    digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    total = right = 0
    while right < len(second_line):
        left = right
        if second_line[right] in digits:
            while right < len(second_line) and second_line[right] in digits:
                right += 1
            if has_adjacent_symbol(first_line, second_line, third_line, left, right):
                total += int("".join(second_line[left:right]))
        right += 1
    return total


def has_adjacent_symbol(first_line, second_line, third_line, left, right):
    possibles = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."}
    if not set(first_line[left - 1 : right + 1]).issubset(possibles):
        return True
    if not set(second_line[left - 1 : right + 1]).issubset(possibles):
        return True
    if not set(third_line[left - 1 : right + 1]).issubset(possibles):
        return True
    return False


if __name__ == "__main__":
    print(part_1())
