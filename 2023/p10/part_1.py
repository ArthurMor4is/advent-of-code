import os

script_directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_directory, "input.txt")

CIRCUIT = None


def part_1():
    s_line, s_column = get_s_position()
    first_position, second_position = get_starts_loop()
    # first_direction, second_direction = "W", "N" # First example
    # first_direction, second_direction = "N", "W" # Second example
    first_direction, second_direction = "N", "W"  # Third example
    result = 1
    while first_position != second_position:
        result += 1
        print(first_position, first_direction)
        first_position, first_direction = get_next_position(
            first_position, first_direction
        )
        print(second_position, second_direction)
        if second_position == [107, 35] and second_direction == "N":
            a = 1
        second_position, second_direction = get_next_position(
            second_position, second_direction
        )
    return result


def get_all_circuit() -> dict[int : dict[int:str]]:
    """
    Ex d[0][0] == 'L'
    """
    result = {}
    with open(file_path, "r") as f:
        line = f.readline().replace("\n", "")
        current_line = 0
        while line:
            result[current_line] = {}
            for current_column, char in enumerate(line):
                result[current_line][current_column] = char
            line = f.readline().replace("\n", "")
            current_line += 1
    return result


CIRCUIT = get_all_circuit()


def get_s_position():
    for line_index, columns in CIRCUIT.items():
        for column_index, char in columns.items():
            if char == "S":
                return line_index, column_index


def get_starts_loop():
    """
    #TODO: Implement general method
    """
    # return [1, 2], [2, 1] #First example
    # return [3, 0], [2, 1] #Second example
    return [110, 28], [109, 29]  # Main case


def get_next_position(position: list[int, int], last_direction) -> list[int, int]:
    line = position[0]
    column = position[1]
    # print(CIRCUIT[line][column])
    if last_direction == "N":
        # | is a vertical pipe connecting north and south.
        if CIRCUIT[line][column] == "|":
            return [position[0] + 1, position[1]], "N"
        # L is a 90-degree bend connecting north and east.
        elif CIRCUIT[line][column] == "L":
            return [position[0], position[1] + 1], "W"
        # J is a 90-degree bend connecting north and west.
        elif CIRCUIT[line][column] == "J":
            return [position[0], position[1] - 1], "E"
    elif last_direction == "S":
        # | is a vertical pipe connecting north and south.
        if CIRCUIT[line][column] == "|":
            return [position[0] - 1, position[1]], "S"
        # 7 is a 90-degree bend connecting south and west.
        elif CIRCUIT[line][column] == "7":
            return [position[0], position[1] - 1], "E"
        # F is a 90-degree bend connecting south and east.
        elif CIRCUIT[line][column] == "F":
            return [position[0], position[1] + 1], "W"
    elif last_direction == "E":
        # - is a horizontal pipe connecting east and west.
        if CIRCUIT[line][column] == "-":
            return [position[0], position[1] - 1], "E"
        # L is a 90-degree bend connecting north and east.
        elif CIRCUIT[line][column] == "L":
            return [position[0] - 1, position[1]], "S"
        # F is a 90-degree bend connecting south and east.
        elif CIRCUIT[line][column] == "F":
            return [position[0] + 1, position[1]], "N"
    elif last_direction == "W":
        # - is a horizontal pipe connecting east and west.
        if CIRCUIT[line][column] == "-":
            return [position[0], position[1] + 1], "W"
        # J is a 90-degree bend connecting north and west.
        elif CIRCUIT[line][column] == "J":
            return [position[0] - 1, position[1]], "S"
        # 7 is a 90-degree bend connecting south and west.
        elif CIRCUIT[line][column] == "7":
            return [position[0] + 1, position[1]], "N"


if __name__ == "__main__":
    print(part_1())
