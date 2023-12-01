# Description: Extract numbers from a file
file_path = './data.txt'

with open(file_path, 'r') as f:
    data = f.read()


def extract_numbers(data):
    current_number = ''
    strings = []
    for char in data:
        if char.isdigit():
            current_number += char
        elif current_number:
            strings.append(current_number)
            current_number = ''
    if current_number:
        strings.append(current_number)
    return strings


print(extract_numbers(data))
