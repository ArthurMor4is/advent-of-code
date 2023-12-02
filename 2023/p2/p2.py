import os
import math

script_directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_directory, "input.txt")


def part_1():
    total = 0
    with open(file_path, "r") as f:
        line = f.readline()
        while line:
            total += check_game(line)
            line = f.readline()
    return total


def check_game(line: str) -> int:
    """Check if is a valid game
    Returns game id if game is valid
    Returns 0 if game is invalid

    Args:
        line (str): One game input

    Returns:
        int: Game id
    """
    cubes_in_bag = {"red": 12, "green": 13, "blue": 14}
    line_splited = line.split(":")
    current_game_id = int(line_splited[0].replace("Game ", ""))
    sort_games = line_splited[1].split(";")
    # Checking the draws
    for draw in sort_games:
        items = draw.split(",")
        for item in items:
            for cube_color, max_count in cubes_in_bag.items():
                current_number_drawn = int(item.split(" ")[1])
                if cube_color in item and current_number_drawn > max_count:
                    return 0
    return current_game_id


def part_2():
    total = 0
    with open(file_path, "r") as f:
        line = f.readline()
        while line:
            total += power_cubes(line)
            line = f.readline()
    return total


def power_cubes(line: str) -> int:
    """The power of a set of cubes is
    equal to the numbers of red, green, and
    blue cubes multiplied together.

    Args:
        line (str): One game input

    Returns:
        int: Power of possible solution
    """
    max_in_bag = {"red": -float("inf"), "green": -float("inf"), "blue": -float("inf")}
    line_splited = line.split(":")
    sort_games = line_splited[1].split(";")
    for draw in sort_games:
        items = draw.split(",")
        for item in items:
            item_splited = item.split(" ")
            current_number_drawn = int(item_splited[1])
            current_color = item_splited[-1].replace("\n", "")
            if current_number_drawn > max_in_bag[current_color]:
                max_in_bag[current_color] = current_number_drawn
    number_of_minimun_cubes = list(max_in_bag.values())
    power_cubes = math.prod(number_of_minimun_cubes)
    return power_cubes


if __name__ == "__main__":
    print(part_1())
    print(part_2())
