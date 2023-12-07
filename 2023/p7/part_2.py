import os

script_directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_directory, "input.txt")

strength = {
    "A": 13,
    "K": 12,
    "Q": 11,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
    "J": 1,
}


def part_2():
    result = 0
    hands_data = get_hands_data()
    data_tuple = [
        (value["type_level"], value["encode"], key) for key, value in hands_data.items()
    ]
    data_tuple.sort()
    for i in range(len(data_tuple)):
        ranking = i + 1
        hand = data_tuple[i][-1]
        result += ranking * hands_data[hand]["bid"]
    return result


def get_hands_data():
    hands_data = {}
    with open(file_path, "r") as f:
        line = f.readline()
        while line:
            hand = get_hand_from_line(line)
            bid = get_bid_from_line(line)
            hand_type_level = get_type_level(hand)
            hand_encoded = get_hand_encoded(hand)
            hands_data[hand] = {
                "type_level": hand_type_level,
                "bid": bid,
                "encode": hand_encoded,
            }
            line = f.readline()
    return hands_data


def get_hand_from_line(line):
    return line.split(" ")[0]


def get_bid_from_line(line):
    bid_text = line.split(" ")[1].replace("\n", "")
    bid_digits = [int(char) for char in bid_text]
    return int("".join(map(str, bid_digits)))


def get_type_level(hand):
    freq_of_kinds = get_frequency_of_kinds(hand)
    list_of_values = list(freq_of_kinds.values())
    list_of_values.sort()
    # Five of a kind, where all five cards have the same label
    if list_of_values == [5]:
        return 6
    # Four of a kind, where four cards have the same label and one card has a different label
    if list_of_values == [1, 4]:
        return 5
    # Full house, where three cards have the same label, and the remaining two cards share a different label
    if list_of_values == [2, 3]:
        return 4
    # Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand
    if list_of_values == [1, 1, 3]:
        return 3
    # Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label
    if list_of_values == [1, 2, 2]:
        return 2
    # One pair, where two cards share one label, and the other three cards have a different label from the pair and each other
    if list_of_values == [1, 1, 1, 2]:
        return 1
    # High card, where all cards' labels are distinct
    if list_of_values == [1, 1, 1, 1, 1] or list_of_values == [1, 1, 1, 1]:
        return 0


def get_frequency_of_kinds(hand):
    result = {}
    for char in hand:
        result[char] = result.get(char, 0) + 1
    if "J" in result:
        max_key = get_max_valid_key(result)
        if max_key == None:
            return result
        result[max_key] += result["J"]
        del result["J"]
    return result


def get_max_valid_key(frequency):
    result = None
    max_value = -float("inf")
    for key, value in frequency.items():
        if value > max_value and key != "J":
            result = key
            max_value = value
    return result


def get_hand_encoded(hand):
    encode = ()
    for char in hand:
        encode = encode + (strength[char],)
    return encode


def update_freq_of_kinds(freq_of_kinds):
    if "J" in freq_of_kinds:
        max_key = max(freq_of_kinds, key=freq_of_kinds.get)
        freq_of_kinds[max_key] += freq_of_kinds.get("J", 0)
        del freq_of_kinds["J"]
    return freq_of_kinds


if __name__ == "__main__":
    print(part_2())
