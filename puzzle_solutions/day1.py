def puzzle_1(file_path: str) -> int:
    with open(file_path, "r", encoding="utf-8") as file:
        contents = file.read()

    # Filter contents to only include digits and newlines
    contents = ''.join(filter(lambda x: x.isdigit() or x == '\n', contents))

    lines = contents.split('\n')
    filtered_lines = []

    for line in lines:
        if len(line) == 1:
            filtered_lines.append(line + line)
        else:
            filtered_lines.append(line[0] + line[-1])



    filtered_lines = [int(line) for line in filtered_lines]
    sum_of_ints = sum(filtered_lines)
    return sum_of_ints

def puzzle_2(file_path: str) -> int:
    # load puzzle input
    file = open(file_path, 'r', encoding="utf-8").read()

    # split puzzle input into a list of lines
    lines = file.split('\n')

    digit_mapping = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
        '1': '1',
        '2': '2',
        '3': '3',
        '4': '4',
        '5': '5',
        '6': '6',
        '7': '7',
        '8': '8',
        '9': '9',
    }

    calibration_value_sum = 0
    for line in lines:
        # find all digits and their positions in a line and append them to a list as tuples
        digit_list = []
        for digit, return_digit in digit_mapping.items():
            pos_iterator = 0
            while line.find(digit, pos_iterator) != -1:
                pos = line.find(digit,pos_iterator)
                digit_list.append((return_digit,pos))
                pos_iterator = pos + len(digit)

        # sort the list of digits by their position
        digit_list = sorted(digit_list, key=lambda x: x[1])

        # find the calibration value and add it to the sum    
        calibration_value_sum += int(''.join([x[0] for x in digit_list][e] for e in (0,-1)))

    return calibration_value_sum

if __name__ == '__main__':
    input_path = '../puzzle_input/day1.txt'
    print(
        "solution 1:", "\n", puzzle_1(input_path), "\n"
        "solution 2:", "\n", puzzle_2(input_path)
        )
