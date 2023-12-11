import os

script_directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_directory, "input.txt")


def part_1():
    space = get_space_input()
    result = get_lenghts_galaxies(space)
    return result


def get_space_input():
    space = {}
    with open(file_path, "r") as f:
        line = f.readline().replace("\n", "")
        current_line = 1
        while line:
            space[current_line] = {}
            for current_column, char in enumerate(line):
                space[current_line][current_column + 1] = char
            line = f.readline().replace("\n", "")
            current_line += 1
    return space


def get_lenghts_galaxies(space):
    result = 0
    empty_lines, empty_columns = get_empty_space_positions(space)
    galaxies_positions = get_galaxies_positions(space, empty_lines, empty_columns)
    # Sum distancies for all pairs
    for i in range(len(galaxies_positions)):
        for j in range(i + 1, len(galaxies_positions)):
            result += abs(galaxies_positions[i][0] - galaxies_positions[j][0])
            result += abs(galaxies_positions[i][1] - galaxies_positions[j][1])
    return result


def get_galaxies_positions(space, empty_lines, empty_columns):
    galaxies_positions = []
    # Finding all galaxies
    for line, columns in space.items():
        for column in columns:
            if space[line][column] == "#":
                new_line, new_column = transform_position(
                    line, column, empty_lines, empty_columns
                )
                galaxies_positions.append([new_line, new_column])
    return galaxies_positions


def transform_position(line, column, empty_lines, empty_columns):
    rate_expansion = 1000000 - 1
    new_line, new_column = line, column
    for l in empty_lines:
        if line > l:
            new_line += rate_expansion
    for c in empty_columns:
        if column > c:
            new_column += rate_expansion
    return new_line, new_column


def get_empty_space_positions(space):
    space_lines = []
    line = 1
    while line <= len(space):
        if set(space[line].values()) == {"."}:
            space_lines.append(line)
        line += 1
    space_columns = []
    column = 1
    while column <= len(space[1]):
        column_elements = [space[line][column] for line in range(1, len(space) + 1)]
        if set(column_elements) == {"."}:
            space_columns.append(column)
        column += 1
    return space_lines, space_columns


if __name__ == "__main__":
    print(part_1())
