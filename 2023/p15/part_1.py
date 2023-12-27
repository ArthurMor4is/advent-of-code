import os

script_directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_directory, "input.txt")


def part_1():
    result = 0
    steps = get_steps_input()
    for step in steps:
        result += get_step_value(step, current_value=0)
    return result


def get_steps_input():
    with open(file_path, "r") as f:
        line = f.readline().replace("\n", "").split(",")
    return line


def get_step_value(step, current_value):
    for char in step:
        current_value += ord(char)
        current_value *= 17
        current_value = current_value % 256
    return current_value


if __name__ == "__main__":
    print(part_1())
