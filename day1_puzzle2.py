file_path = "advent_input/day1.txt"
file = open(file_path, 'r').read()
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
for i in range(len(lines)):
    digit_list = []
    for digit, return_digit in digit_mapping.items():
        pos_iterator = 0
        while lines[i].find(digit, pos_iterator) != -1:
            pos = lines[i].find(digit,pos_iterator)
            digit_list.append((return_digit,pos))
            pos_iterator = pos + len(digit)
    digit_list = sorted(digit_list, key=lambda x: x[1])
    # sick ass list comprehension, creates a list per digit and only picks the first item of the tuple (drops the pos)
    # and then picks 1st and last item of each list
    # also concats the list values using an assignment expression
    calibration_value = ''
    [calibration_value := calibration_value + x for x in [[x[0] for x in digit_list][e] for e in (0,-1)]]
    calibration_value_sum += int(calibration_value)
    # print(sorted(digit_list.items(), key=lambda x: x[1]))

print(calibration_value_sum)
