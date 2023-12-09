import os

script_directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_directory, "input.txt")


def part_1():
    result = 0
    with open(file_path, "r") as f:
        line = f.readline()
        while line:
            line_chars = line.replace("\n", "").split(" ")
            line_numbers = [int(char) for char in line_chars]
            result += get_next_value(line_numbers)
            line = f.readline()
    return result


def get_next_value(history):
    first_elements = []
    current_differences = history.copy()
    while any(element != 0 for element in current_differences):
        first_elements.append(current_differences[0])
        for i in range(1, len(current_differences)):
            current_differences[i - 1] = (
                current_differences[i] - current_differences[i - 1]
            )
        current_differences = current_differences[:-1]
    result = first_elements[0]
    for i in range(1, len(first_elements)):
        if i % 2 == 0:
            result += first_elements[i]
        else:
            result -= first_elements[i]
    return result


if __name__ == "__main__":
    print(part_1())
