output_lines = []

with open('01-12/data.txt', 'r') as file:
    for line in file:
        result_string = ''.join(filter(str.isdigit, line))
        output_lines.append(result_string)

with open('01-12/output.txt', 'w') as output_file:
    for line in output_lines:
        output_file.write(line + '\n')
