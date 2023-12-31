import os

script_directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_directory, "input.txt")


def part_1():
    lowest_location = float("inf")
    with open(file_path, "r") as f:
        seeds = get_seeds()
        for seed in seeds:
            seed_location = get_location(seed)
            if seed_location < lowest_location:
                lowest_location = seed_location
    return lowest_location


def get_seeds():
    with open(file_path, "r") as f:
        line = f.readline()
        seeds_text = line[:-1].split(":")[-1].split(" ")[1:]
    return [int(number) for number in seeds_text]


def get_location(seed):
    destination = seed
    with open(file_path, "r") as f:
        line = f.readline()
        while line:
            maps_lines = []
            if "map" in line:
                while line != "\n" and line:
                    maps_lines.append(line)
                    line = f.readline()
                destination = get_destination_from_map(
                    maps_lines[1:], source=destination
                )
            line = f.readline()
    return destination


def get_destination_from_map(maps_lines, source):
    destination = source
    for line in maps_lines:
        d_start_range, s_start_range, r = get_frontiers(line)
        destination, found_range = get_destination_from_line(
            d_start_range, s_start_range, r, source=destination
        )
        if found_range:
            break
    return destination


def get_frontiers(line):
    line_replaced = line.replace("\n", "")
    line_splited = line_replaced.split(" ")
    return int(line_splited[0]), int(line_splited[1]), int(line_splited[2])


def get_destination_from_line(d_start_range, s_start_range, r, source):
    shift_source_to_destination = d_start_range - s_start_range
    destination = source
    found_range = False
    if s_start_range + r > source >= s_start_range:
        destination = source + shift_source_to_destination
        found_range = True
    return destination, found_range


if __name__ == "__main__":
    print(part_1())
