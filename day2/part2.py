def is_safe(report):
    increasing = all(report[i] < report[i+1] for i in range(len(report)-1))
    decreasing = all(report[i] > report[i+1] for i in range(len(report)-1))

    differences_valid = all(1 <= abs(report[i] - report[i+1]) <= 3 for i in range(len(report)-1))

    return (increasing or decreasing) and differences_valid

def is_safe_with_dampener(report):
    if is_safe(report):
        return True

    for i in range(len(report)):
        new_report = report[:i] + report[i+1:]
        if is_safe(new_report):
            return True
    return False

def count_safe_reports(reports):
    safe_count = 0
    for report in reports:
        if is_safe_with_dampener(report):
            safe_count += 1
    return safe_count

def read_input_file(file_name):
    with open(file_name, 'r') as file:
        reports = []
        for line in file:
            reports.append(list(map(int, line.split())))
    return reports

file_name = 'input.txt'
reports = read_input_file(file_name)

print(count_safe_reports(reports))
