# load puzzle input
file_path = "advent_input/day1.txt"
file = open(file_path, 'r').read()

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
for i in range(len(lines)):
    # find all digits and their positions in a line and append them to a list as tuples
    digit_list = []
    for digit, return_digit in digit_mapping.items():
        pos_iterator = 0
        while lines[i].find(digit, pos_iterator) != -1:
            pos = lines[i].find(digit,pos_iterator)
            digit_list.append((return_digit,pos))
            pos_iterator = pos + len(digit)

    # sort the list of digits by their position
    digit_list = sorted(digit_list, key=lambda x: x[1])
    
    # create a string of the first and last digits
    calibration_value = ''
    [calibration_value := calibration_value + x for x in # concatenate the 1st and last digits with the walrus operator
        [
            [x[0] for x in digit_list] # create a list of the 1st item of each tuple, I.E. the digits
            [e] for e in (0,-1) 
        ] # create a list with only the 1st and last item in the list of digits
    ]
    
    # add each calibration value to the sum
    calibration_value_sum += int(calibration_value)

print(calibration_value_sum)