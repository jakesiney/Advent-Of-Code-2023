# Description: Advent of Code - Day 1: Trebuchet - Part Two

just_numbers = []


def part_two_b(data):
    word_mapping = {
        'one': 'o1e',
        'two': 't2o',
        'three': 't3e',
        'four': 'f4r',
        'five': 'f5e',
        'six': 's6x',
        'seven': 's7n',
        'eight': 'e8t',
        'nine': 'n9e',
    }

    for line in data:
        for word, replacement in word_mapping.items():
            line = line.replace(word, replacement)
        just_numbers.append(line)
    return just_numbers


with open('Day-1/Part-2-A/output.txt', 'r') as f:
    data = f.readlines()


just_numbers = part_two_b(data)

with open('Day-1/Part-2-B/output.txt', 'w') as output_file:
    for line in just_numbers:
        output_file.write(line)
