import os

script_directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_directory, "input.txt")


def part_1():
    result = 0
    sequence_of_directions = get_sequence_directions()
    result = get_steps_to_zzz(sequence_of_directions)
    return result


def get_sequence_directions():
    with open(file_path, "r") as f:
        line = f.readline()
    return line.replace("\n", "")


def get_map_of_directions():
    directions = {}
    with open(file_path, "r") as f:
        line = f.readline()
        while "=" not in line:
            line = f.readline()
        while line:
            line_split = line.split(" = ")
            origin = line_split[0]
            destinations = (
                line_split[1]
                .replace("(", "")
                .replace(")", "")
                .replace("\n", "")
                .split(", ")
            )
            directions[origin] = {"L": destinations[0], "R": destinations[1]}
            line = f.readline()
    return directions


MAP_OF_DIRECTIONS = get_map_of_directions()


def get_steps_to_zzz(sequence_of_directions):
    step = 0
    first_position = "AAA"
    direction = get_direction(sequence_of_directions, step)
    position = get_next_position(position=first_position, direction=direction)
    step += 1
    while position != "ZZZ":
        direction = sequence_of_directions[step % len(sequence_of_directions)]
        position = get_next_position(position=position, direction=direction)
        step += 1
    return step


def get_direction(sequence_of_directions, step):
    return sequence_of_directions[step % len(sequence_of_directions)]


def get_next_position(position, direction):
    current_position_info = MAP_OF_DIRECTIONS[position]
    next_position = current_position_info[direction]
    return next_position


if __name__ == "__main__":
    print(part_1())
