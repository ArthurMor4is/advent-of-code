import os

script_directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_directory, "input.txt")


def part_1():
    result = 0
    columns = get_space_input_as_columns()
    new_columns = move_all_rocks(columns)
    for column in new_columns:
        result += count_load_columns(column)
    return result

def get_space_input_as_columns():
    with open(file_path, "r") as f:
        line = f.readline().replace("\n", "")
        columns = []
        for i in range(len(line)):
            columns.append([])
        while line:
            elements = line.replace("\n", "")
            for index, column in enumerate(columns):
                column.append(elements[index]) 
            line = f.readline()
    return columns

def move_all_rocks(columns):    
    for index, column in enumerate(columns):
        columns[index] = new_column(column)
    return columns

def new_column(column):
    for current_index in range(len(column)):
        if column[current_index] == 'O':
            last_wall = -1
            for i in range(0, current_index):
                if column[i] in ['O', '#']:
                    last_wall = i
            if last_wall + 1 != current_index:
                column[last_wall + 1] = 'O'
                column[current_index] = '.'
    return column

def count_load_columns(column):
    n_lines = len(column)
    result = 0
    for index, element in enumerate(column):
        mult = n_lines - index
        if element == 'O':
            result += mult
    return result
            

if __name__ == "__main__":
    print(part_1())
