# Description: Advent of Code - Day 1: Trebuchet - Part Two

just_numbers = []


def part_two(data):
    word_mapping = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
        'ten': '10'
    }

    for line in data:
        for word, replacement in word_mapping.items():
            line = line.replace(word, replacement)
        just_numbers.append(line)
    return just_numbers


with open('Day-1/data.txt', 'r') as f:
    data = f.readlines()

# Call the function to populate just_numbers list
just_numbers = part_two(data)

with open('Day-1/part_two_output.txt', 'w') as output_file:
    for line in just_numbers:
        output_file.write(line)
