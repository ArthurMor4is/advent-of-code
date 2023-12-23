import os

script_directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_directory, "input.txt")


def part_1():
    result = 0
    conditions, inputs = get_inputs()
    for input in inputs:
        result += get_rating(input, conditions)
    return result

def get_rating(input, conditions):
    current_state = 'in'
    while current_state not in ('A', 'R'):
        current_state = get_next_state(input, current_state, conditions)        
    if current_state == 'A':
        rating = compute_rating(input)
        return rating
    return 0

def get_next_state(input, current_state, conditions):
    state_conditions = conditions[current_state]
    for value in input:
        exec(value)
    for condition in state_conditions[:-1]:
        check_condition = condition.split(':')[0]
        if eval(check_condition):
            return condition.split(':')[1]
    return state_conditions[-1]

def compute_rating(input):
    total = 0
    for value in input:
        total += int(value.split('=')[1])
    return total

def get_inputs():
    with open(file_path, "r") as file:
        conditions = {}
        parts = []
        all_conditions = False
        for line in file: 
            if not all_conditions:
                if line == '\n':
                    all_conditions = True
                    continue
                split_line = line[:-2].split('{')
                conditions[split_line[0]] = split_line[1].split(',')
            else:
                parts.append(line[1:-2].split(','))
    return conditions, parts


if __name__ == "__main__":
    print(part_1())
    