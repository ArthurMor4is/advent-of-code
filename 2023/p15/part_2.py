import os

script_directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_directory, "input.txt")


def part_1():
    boxes = {box_number: [] for box_number in range(256)}
    steps = get_steps_input()
    for step in steps:
        if "=" in step:
            boxes = put_step_to_box(step, boxes)
        elif "-" in step:
            boxes = remove_step_from_box(step, boxes)
    return get_focus_power(boxes)


def put_step_to_box(step, boxes):
    split_step = step.split("=")
    label = split_step[0]
    focal_length = split_step[1]
    box_number = get_step_value(label)
    for index, element in enumerate(boxes[box_number]):
        if label in element:
            boxes[box_number][index][label] = int(focal_length)
            return boxes
    boxes[box_number].append({label: int(focal_length)})
    return boxes


def remove_step_from_box(step, boxes):
    split_step = step.split("-")
    label = split_step[0]
    box_number = get_step_value(label)
    for element in boxes[box_number]:
        if label in element:
            boxes[box_number].remove(element)
    return boxes


def get_steps_input():
    with open(file_path, "r") as f:
        line = f.readline().replace("\n", "").split(",")
    return line


def get_step_value(step, current_value=0):
    for char in step:
        current_value += ord(char)
        current_value *= 17
        current_value = current_value % 256
    return current_value


def get_focus_power(boxes):
    result = 0
    for box, elements in boxes.items():
        for slot_position, element in enumerate(elements):
            result += (box + 1) * (slot_position + 1) * list(element.values())[0]
    return result


if __name__ == "__main__":
    print(part_1())
