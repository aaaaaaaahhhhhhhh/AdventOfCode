def parse_input(data):
    sections = data.strip().split("\n\n")
    rules = [tuple(map(int, line.split('|'))) for line in sections[0].strip().split('\n')]
    updates = [list(map(int, line.split(','))) for line in sections[1].strip().split('\n')]
    return rules, updates

def is_update_valid(update, rules):
    # Create a map of the indices of the update pages
    index_map = {page: i for i, page in enumerate(update)}
    for x, y in rules:
        # If both pages are in the update, ensure x comes before y
        if x in index_map and y in index_map and index_map[x] > index_map[y]:
            return False
    return True

def reorder_update(update, rules):
    # Sort the update based on the rules
    def custom_order(page):
        # Assign a priority based on the rules
        priority = 0
        for x, y in rules:
            if page == x:
                priority -= 1
            elif page == y:
                priority += 1
        return priority

    return sorted(update, key=custom_order)

def find_middle_page(update):
    return update[len(update) // 2]

def solve(file_path):
    with open(file_path, 'r') as file:
        data = file.read()
    rules, updates = parse_input(data)
    total = 0

    for update in updates:
        if not is_update_valid(update, rules):
            corrected_update = reorder_update(update, rules)
            middle_page = find_middle_page(corrected_update)
            total += middle_page

    return total

# Run the solution with "input.txt"
if __name__ == "__main__":
    result = solve("input.txt")
    print(result)
