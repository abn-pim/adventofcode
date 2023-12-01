file_path = "advent_input/day1.txt"

with open(file_path, "r") as file:
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
print(sum_of_ints)


