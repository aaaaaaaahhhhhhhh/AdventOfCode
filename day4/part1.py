def count_word_occurrences_from_file(file_path, word):
    with open(file_path, "r") as file:
        grid = [list(line.strip()) for line in file.readlines()]
    
    rows, cols = len(grid), len(grid[0])
    word_len = len(word)
    directions = [
        (0, 1),   # Right
        (0, -1),  # Left
        (1, 0),   # Down
        (-1, 0),  # Up
        (1, 1),   # Diagonal down-right
        (1, -1),  # Diagonal down-left
        (-1, 1),  # Diagonal up-right
        (-1, -1)  # Diagonal up-left
    ]
    count = 0

    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols

    for i in range(rows):
        for j in range(cols):
            for dx, dy in directions:
                match = True
                for k in range(word_len):
                    nx, ny = i + k * dx, j + k * dy
                    if not is_valid(nx, ny) or grid[nx][ny] != word[k]:
                        match = False
                        break
                if match:
                    count += 1

    return count

# Example usage: read from "input.txt" and count occurrences of "XMAS"
input_file_path = "./input.txt"
word_to_find = "XMAS"
occurrences = count_word_occurrences_from_file(input_file_path, word_to_find)
print(occurrences)
