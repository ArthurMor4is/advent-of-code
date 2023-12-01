def main():
    total = 0
    with open('input.txt', 'r') as f:
        line = f.readline()
        while line:
            digits = [int(char) for char in line if char.isdigit()]
            cal_value = 10*digits[0] + digits[-1]
            total += cal_value
            line = f.readline()
    return total

if __name__ == '__main__':
    print(main())