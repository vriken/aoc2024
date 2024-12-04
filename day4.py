with open('/Users/akeros/Downloads/input.txt', 'r') as file:
    data = file.read().strip().split('\n')

def count_XMAS(grid):
    rows = len(grid)
    cols = len(grid[0])
    count = 0

    x_pos = []
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 'X':
                x_pos.append((row, col))

    for row, col in x_pos:
        # right
        count += check_line(grid, row, col, 0, 1)
        # left
        count += check_line(grid, row, col, 0, -1)
        # down
        count += check_line(grid, row, col, 1, 0)
        # up
        count += check_line(grid, row, col, -1, 0)
        # diagonal down-right
        count += check_line(grid, row, col, 1, 1)
        # diagonal up-left
        count += check_line(grid, row, col, -1, -1)
        # diagonal down-left
        count += check_line(grid, row, col, 1, -1)
        # diagonal up-right
        count += check_line(grid, row, col, -1, 1)

    return count

def check_line(grid, row, col, dx, dy):
    count = 0
    if is_valid_position(row + 3*dx, col + 3*dy, len(grid), len(grid[0])):
        if grid[row+dx][col+dy] == 'M' and \
           grid[row+2*dx][col+2*dy] == 'A' and \
           grid[row+3*dx][col+3*dy] == 'S':
            count += 1

    return count

def is_valid_position(row, col, rows, cols):
    return 0 <= row < rows and 0 <= col < cols

grid = [list(line) for line in data]
print(count_XMAS(grid))