import re

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

# lines = ["xtwone3four","12bruhoneone3","1yoyo5six"]

sum = 0

for i in range(len(lines)):
    digit_list = []
    for digit, return_digit in digit_mapping.items():
        pos_iterator = 0
        while lines[i].find(digit, pos_iterator) != -1:
            pos = lines[i].find(digit,pos_iterator)
            digit_list.append((return_digit,pos))
            pos_iterator = pos + len(digit)
    # print(digit_list)
    digit_list = sorted(digit_list, key=lambda x: x[1])
    # print(sorted_list)
    digit_list = [x[0] for x in digit_list]
    calibration_value = digit_list[0] + digit_list[-1]
    sum = sum + int(calibration_value)
    # print(sorted(digit_list.items(), key=lambda x: x[1]))

print(sum)
