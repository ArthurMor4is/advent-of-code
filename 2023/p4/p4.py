import os

script_directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_directory, "input.txt")


def part_1():
    result = 0
    with open(file_path, "r") as f:
        line = f.readline()
        while line:
            result += points_in_card(line)
            line = f.readline()
    return result


def points_in_card(line):
    my_winning_numbers = get_my_winning_numbers(line)
    if my_winning_numbers > 0:
        return 2 ** (my_winning_numbers - 1)
    return 0


def get_my_winning_numbers(line):
    card_split = line.split(":")[-1]
    numbers_split = card_split.split("|")
    my_winning_numbers = 0
    my_numbers = [int(char) for char in numbers_split[0].split(" ") if char != ""]
    wining_numbers = set(
        [int(char) for char in numbers_split[1].split(" ") if char != ""]
    )
    for number in my_numbers:
        if number in wining_numbers:
            my_winning_numbers += 1
    return my_winning_numbers


def part_2():
    cards_logs = building_cards_count()
    # Building cards_logs dict
    with open(file_path, "r") as f:
        line = f.readline()
        while line:
            cards_logs = update_cards_count(line, cards_logs)
            line = f.readline()
    cards_count = list(cards_logs.values())
    return sum(cards_count)


def building_cards_count():
    cards = 0
    cards_logs = {}
    # Building cards_logs dict
    with open(file_path, "r") as f:
        line = f.readline()
        while line:
            cards += 1
            cards_logs[cards] = 1
            line = f.readline()
    return cards_logs


def update_cards_count(line, cards_logs):
    current_card_number = int(line.split(":")[0].split(" ")[-1])
    my_winning_numbers = get_my_winning_numbers(line)
    for _ in range(cards_logs[current_card_number]):
        for card_number in range(
            current_card_number + 1, current_card_number + 1 + my_winning_numbers
        ):
            cards_logs[card_number] += 1
    return cards_logs


if __name__ == "__main__":
    print(part_1())
    print(part_2())
