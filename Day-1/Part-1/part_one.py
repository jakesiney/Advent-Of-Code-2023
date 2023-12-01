# Description: Advent of Code - Day 1: Trebuchet - Part One

def part_one(calibrations):
    total = 0
    for calibration in calibrations:
        if len(calibration.strip()) == 1:
            total += int(calibration.strip() + calibration.strip())
        else:
            total += int(calibration.strip()[0] + calibration.strip()[-1])
    return total


with open('Day-1/output.txt', 'r') as file:
    calibrations = file.readlines()

print(part_one(calibrations))
