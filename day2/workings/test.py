counter = 0

with open("input.txt", "r") as file:
    for line in file:
        values = list(map(int, line.split()))  # Convert to integers

        # Check if the values are sorted (ascending or descending)
        if values == sorted(values) or values == sorted(values, reverse=True):
            # Check if the differences are within the range [1, 3]
            if all(1 <= abs(values[i] - values[i + 1]) <= 3 for i in range(len(values) - 1)):
                counter += 1  # Only increment if both conditions are met

print(counter)
