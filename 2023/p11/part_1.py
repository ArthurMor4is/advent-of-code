import os

script_directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_directory, "input.txt")


def part_1():
    space = get_space_input()
    space = expand_space(space)
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


def expand_space(space):
    # Expands lines
    line = 1
    while line <= len(space):
        if set(space[line].values()) == {"."}:
            for i in range(len(space) + 1, line, -1):
                space[i] = space[i - 1]
            line += 2
        else:
            line += 1
    # Expands columns
    column = 1
    while column <= len(space[1]):
        initial_columns = len(space[1])
        column_elements = [space[line][column] for line in range(1, len(space) + 1)]
        if set(column_elements) == {"."}:
            for line in range(1, len(space) + 1):
                for i in range(initial_columns + 1, column, -1):
                    space[line][i] = space[line][i - 1]
            column += 2
        else:
            column += 1
    return space


def get_lenghts_galaxies(space):
    result = 0
    galaxies_positions = []
    # Finding all galaxies
    for line, columns in space.items():
        for column in columns:
            if space[line][column] == "#":
                galaxies_positions.append([line, column])
    # Sum distancies for all pairs
    for i in range(len(galaxies_positions)):
        for j in range(i + 1, len(galaxies_positions)):
            result += abs(galaxies_positions[i][0] - galaxies_positions[j][0])
            result += abs(galaxies_positions[i][1] - galaxies_positions[j][1])
    return result


if __name__ == "__main__":
    print(part_1())
