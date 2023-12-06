import os

script_directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_directory, "input.txt")


def part_2():
    # seeds_list = get_seeds_from_range()
    result_map = get_result_map()
    return None
    return get_lowest_location(seeds_list, result_map)


def get_result_map():
    with open(file_path, "r") as f:
        line = f.readline()
        result_map = {}
        while line:
            if "map" in line:
                current_map_config = []
                line = f.readline()
                while line != "\n" and line:
                    current_line_numbers = [
                        int(number) for number in line.replace("\n", "").split(" ")
                    ]
                    current_map_config.append(current_line_numbers)
                    line = f.readline()
                current_map = create_current_map(current_map_config)
                result_map = update_result_from_map(result_map, current_map)
            line = f.readline()
    return result_map


def create_current_map(input_map):
    current_map = {}
    for line in input_map:
        current_map = update_result_from_line(current_map, line)
    return current_map


def update_result_from_line(result_map, line):
    destination_range_start = line[0]
    source_range_start = line[1]
    for i in range(line[-1]):
        result_map[source_range_start + i] = destination_range_start + i
    return result_map


def update_result_from_map(result_map, current_map):
    for key, value in result_map.items():
        if value in current_map.keys():
            result_map[key] = current_map[value]
    for key, value in current_map.items():
        if key not in result_map.keys():
            result_map[key] = value
    return result_map


def get_lowest_location(seeds_list, result_map):
    lowest_location = float("inf")
    for seed in seeds_list:
        location = result_map[seed]
        if location < lowest_location:
            lowest_location = location
    return lowest_location


def get_seeds_from_range():
    seeds = set()
    with open(file_path, "r") as f:
        line = f.readline()
        seeds_text = line[:-1].split(":")[-1].split(" ")[1:]
    p = 0
    q = 1
    while q < len(seeds_text):
        seed_p = int(seeds_text[p])
        seed_range = int(seeds_text[q])
        for i in range(seed_range):
            seeds.add(seed_p + i)
        p += 2
        q += 2
    return list(seeds)


if __name__ == "__main__":
    print(part_2())
