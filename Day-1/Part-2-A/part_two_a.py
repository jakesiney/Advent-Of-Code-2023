oneeightsfixed = []


def part_two_a(data):
    word_mapping = {
        'oneight': 'oneeight',
    }
    for line in data:
        for word, replacement in word_mapping.items():
            line = line.replace(word, replacement)
        oneeightsfixed.append(line)
    return oneeightsfixed


with open('Day-1/data.txt', 'r') as f:
    data = f.readlines()

oneeightsfixed = part_two_a(data)

with open('Day-1/Part-2-A/output.txt', 'w') as output_file:
    for line in oneeightsfixed:
        output_file.write(line)
