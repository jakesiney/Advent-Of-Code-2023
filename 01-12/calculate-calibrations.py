def calculate_calibrations(calibrations):
    total = 0
    for calibration in calibrations:
        if len(calibration.strip()) == 1:
            total += int(calibration.strip() + calibration.strip())
        else:
            total += int(calibration.strip()[0] + calibration.strip()[-1])
    return total


with open('01-12/output.txt', 'r') as file:
    calibrations = file.readlines()

print(calculate_calibrations(calibrations))
