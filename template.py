import os

script_directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_directory, "input.txt")


def part_1():
    result = None
    with open(file_path, "r") as f:
        line = f.readline()
        while line:
            # Some logic here
            line = f.readline()
    return result


def part_2():
    result = None
    with open(file_path, "r") as f:
        line = f.readline()
        while line:
            # Some logic here
            line = f.readline()
    return result


if __name__ == "__main__":
    print(part_1())
    print(part_2())
