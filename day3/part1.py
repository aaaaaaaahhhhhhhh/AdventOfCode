import re
with open("input.txt", "r") as file:
    lines = file.readlines()
    memory = "".join(lines).replace("\n", "")
# Simulated input (or read from file)

# Regex to match valid mul instructions with two numbers
    matches = re.finditer(r"mul\((\d{1,3}),(\d{1,3})\)", memory)

# Initialize the total sum
    total = 0

# Process each valid match
    for match in matches:
        x, y = int(match.group(1)), int(match.group(2))  # Extract and convert each number
        result = x * y
        print(f"Matched: {match.group(0)}, Result: {result}")
        total += result

# Output the total sum
print("Total Sum:", total)
