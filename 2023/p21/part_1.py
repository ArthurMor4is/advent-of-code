import os

script_directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_directory, "input.txt")


def part_1():
    map = get_map()
    steps = 64
    for _ in range(steps):
        map = step(map)
        result = count_plots(map)
    return result


def print_map(map):
    for line in map:
        print("".join(line))


def get_map():
    map = []
    with open(file_path, "r") as f:
        line = f.readline().replace("\n", "")
        while line:
            # Some logic here
            map.append(list(line))
            line = f.readline().replace("\n", "")
    return map


def step(map):
    s_locations = []
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == "S":
                s_locations.append((i, j))
    map = step_s(map, s_locations)
    return map


def step_s(map, s_locations):
    update_positions = {location: [] for location in s_locations}
    for location in s_locations:
        # Finding new positions
        # North
        if map[location[0] - 1][location[1]] == ".":
            update_positions[location].append((location[0] - 1, location[1]))
        # East
        if map[location[0]][location[1] + 1] == ".":
            update_positions[location].append((location[0], location[1] + 1))
        # South
        if map[location[0] + 1][location[1]] == ".":
            update_positions[location].append((location[0] + 1, location[1]))
        # West
        if map[location[0]][location[1] - 1] == ".":
            update_positions[location].append((location[0], location[1] - 1))
    # Updating map
    for key in update_positions.keys():
        for value in update_positions[key]:
            map[value[0]][value[1]] = "S"
            map[key[0]][key[1]] = "."
    return map


def count_plots(map):
    # Count S plots
    result = 0
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == "S":
                result += 1
    return result


if __name__ == "__main__":
    print(part_1())
