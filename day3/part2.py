import re

total = 0

with open('input.txt', 'r') as file:
    lines = file.readlines()
    line = ''.join(lines).replace('\n', '')

    # Regex to remove everything between don't() and do()
    do_matches = re.findall(r"don't\(\).*?do\(\)", line)
    for match in do_matches:
        line = line.replace(match, '')

    # Regex to extract the mul() statements
    mul_matches = re.findall(r"mul\((\d+),(\d+)\)", line)
    for match in mul_matches:
        total += (int(match[0]) * int(match[1]))

print(total)
