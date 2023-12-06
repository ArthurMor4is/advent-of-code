import os

script_directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_directory, "input.txt")


def part_1():
    result = None
    with open(file_path, "r") as f:
        times = get_times(f.readline())
        distances = get_distances(f.readline())
        result = get_total_options(times, distances)
    return result

def part_2():
    result = None
    with open(file_path, "r") as f:
        unique_time = get_unique_time(f.readline())
        unique_distance = get_unique_distance(f.readline())
        result = get_total_options([unique_time], [unique_distance])
    return result

def get_unique_time(line):
    chars = line.replace("\n", "").split(":")[-1].split("  ")[:]
    result = ''
    for char in chars:
        if char != "":
            result += char
    return int(result.replace(" ", ""))


def get_unique_distance(line):
    chars = line.replace("\n", "").split(":")[-1].split("  ")[:]
    result = ''
    for char in chars:
        if char != "":
            result += char
    return int(result.replace(" ", ""))

def get_times(line):
    chars = line.replace("\n", "").split(":")[-1].split("  ")[:]
    result = []
    for char in chars:
        if char != "":
            result.append(int(char))
    return result

def get_distances(line):
    chars = line.replace("\n", "").split(":")[-1].split("  ")[:]
    result = []
    for char in chars:
        if char != "":
            result.append(int(char))
    return result

def get_total_options(times, distances):
    """
    Equations:
    v_zero = t_zero
    t_zero + t_one = T
    total_distance = v_zero * t_one
    """
    total_ways = []
    for i in range(len(times)):
        current_ways = 0
        T = times[i]
        record = distances[i]
        for t_holding in range(T):
            if t_holding*(T - t_holding) > record:
                current_ways += 1
        total_ways.append(current_ways)
    result = 1
    for number in total_ways:
        result *= number
    return result

if __name__ == "__main__":
    print(part_1())
    print(part_2())
