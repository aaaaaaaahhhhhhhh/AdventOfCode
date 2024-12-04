def count_xmas_patterns(grid):
    rows = len(grid)
    cols = len(grid[0])
    pattern_count = 0

    # Helper function to check if a MAS exists at a given row and column
    def is_mas(r, c):
        if 0 <= r < rows and 0 <= c + 2 < cols:
            return grid[r][c] == 'M' and grid[r][c + 1] == 'A' and grid[r][c + 2] == 'S'
        return False

    # Check for the X-MAS pattern
    for r in range(rows - 2):  # We only check until rows - 2 to prevent out-of-bound errors
        for c in range(cols - 2):  # We check columns until cols - 2
            top_mas = is_mas(r, c)
            center_a = grid[r + 1][c + 1] == 'A' if 0 <= r + 1 < rows and 0 <= c + 1 < cols else False
            bottom_mas = is_mas(r + 2, c)
            if top_mas and center_a and bottom_mas:
                print(f"X-MAS pattern found at top-left corner ({r}, {c})")
                pattern_count += 1

    return pattern_count


# Reading input from a file for convenience
def read_grid_from_file(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file.readlines()]


if __name__ == "__main__":
    # Replace 'input.txt' with your input file
    grid = read_grid_from_file("test.txt")
    grid = [list(row) for row in grid]  # Convert to a list of lists for easier indexing

    # Print the grid for debugging
    print("Grid Loaded:")
    for row in grid:
        print("".join(row))

    # Compute rows and columns for debugging
    rows = len(grid)
    cols = len(grid[0])
    print(f"Rows: {rows}, Columns: {cols}")

    # Count and display the X-MAS patterns
    result = count_xmas_patterns(grid)
    print("Number of X-MAS patterns:", result)
