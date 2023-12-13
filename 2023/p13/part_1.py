import os

script_directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_directory, "input.txt")


def part_1():
    result = 0
    with open(file_path, "r") as f:
        line = f.readline()
        while line:
            if line and line != "\n":
                space_input, line = get_space_input(f, line)
                temp = result_lines(space_input)
                if temp:
                    result += temp
                else:
                    result += result_columns(space_input)
            else:
                line = f.readline()
    return result


def get_space_input(f, line):
    space = {}
    current_line = 1
    while len(line) > 0 and line != "\n":
        cleaned_line = line.replace("\n", "")
        space[current_line] = {}
        for current_column, char in enumerate(cleaned_line):
            space[current_line][current_column + 1] = char
        line = f.readline()
        current_line += 1
    return space, line


def result_columns(space_input):
    columns = []
    for k in range(1, len(space_input[1]) + 1):
        current_column = []
        for i in range(1, len(space_input) + 1):
            current_column.append(space_input[i][k])
        columns.append(hash("".join(current_column)))
    return get_index_of_palindrome(columns)


def result_lines(space_input):
    lines = []
    for i in range(1, len(space_input) + 1):
        current_line = list(space_input[i].values())
        lines.append(hash("".join(current_line)))
    index = get_index_of_palindrome(lines)
    if index:
        return index * 100


def get_index_of_palindrome(sequence):
    for i in range(len(sequence) - 1):
        j = len(sequence)
        subsequence = sequence[i:j]
        if len(subsequence) % 2 == 0 and is_palindrome(subsequence):
            center_position = i + ((j - i) // 2)
            return center_position
    for j in range(len(sequence), 1, -1):
        i = 0
        subsequence = sequence[i:j]
        if len(subsequence) % 2 == 0 and is_palindrome(subsequence):
            center_position = i + ((j - i) // 2)
            return center_position


def is_palindrome(subsequence):
    return subsequence == subsequence[::-1]


if __name__ == "__main__":
    print(part_1())
