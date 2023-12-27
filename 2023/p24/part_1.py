import os

script_directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_directory, "input.txt")

from itertools import combinations


def part_1():
    result = 0
    hailstones = get_hailstones_equations()
    # limit = (7, 27)
    limit = (200000000000000, 400000000000000)
    for combination in combinations(hailstones, 2):
        result += (
            1
            if colide_inside_limit_in_future(
                hail_1=combination[0], hail_2=combination[1], limit=limit
            )
            else 0
        )
    return result


def colide_inside_limit_in_future(hail_1, hail_2, limit):
    x_intersection, y_intersection, intercept = get_intersection(hail_1, hail_2)
    if not intercept:
        return False
    if x_intersection > limit[1] or x_intersection < limit[0]:
        return False
    if y_intersection > limit[1] or y_intersection < limit[0]:
        return False
    t_a = (x_intersection - hail_1["position"][0]) / hail_1["velocity"][0]
    t_b = (x_intersection - hail_2["position"][0]) / hail_2["velocity"][0]
    if t_a < 0 or t_b < 0:
        return False
    return True


def get_intersection(hail_1, hail_2):
    hail_1_parameters = hail_1["parameters"]
    hail_2_parameters = hail_2["parameters"]
    if hail_1_parameters[0] == hail_2_parameters[0]:
        return 0, 0, False
    x_intersection = (hail_2_parameters[1] - hail_1_parameters[1]) / (
        hail_1_parameters[0] - hail_2_parameters[0]
    )
    y_intersection = hail_1_parameters[0] * x_intersection + hail_1_parameters[1]
    return x_intersection, y_intersection, True


def get_hailstones_equations():
    hailstones = []
    with open(file_path, "r") as f:
        line = f.readline().replace("\n", "")
        while line:
            # Some logic here
            line_split = line.split("@")
            position = tuple([int(char) for char in line_split[0].split(",")])
            velocity = tuple([int(char) for char in line_split[1].split(",")])
            (
                a,
                b,
            ) = get_equations_parameters(position, velocity)
            hailstones.append(
                {"velocity": velocity, "parameters": (a, b), "position": position}
            )
            line = f.readline()
    return hailstones


def get_equations_parameters(position, velocity):
    a = velocity[1] / velocity[0]
    b = position[1] - a * position[0]
    return a, b


if __name__ == "__main__":
    print(part_1())
