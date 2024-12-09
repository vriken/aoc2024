with open('C:\\Users\\vrike\\Downloads\\input.txt', 'r') as file:
    data = file.read().strip().split('\n')

def find_loop_positions(grid):
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # Up, Right, Down, Left
    direction_index = 0

    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell in ['^', '>', 'v', '<']:
                start_pos = (i, j)
                if cell == '^':
                    direction_index = 0
                elif cell == '>':
                    direction_index = 1
                elif cell == 'v':
                    direction_index = 2
                elif cell == '<':
                    direction_index = 3
                break

    def simulate_with_obstruction(obstruction):
        visited = set()
        x, y = start_pos
        visited.add((x, y))
        direction_idx = direction_index

        while 0 <= x < len(grid) and 0 <= y < len(grid):
            dx, dy = directions[direction_idx]
            nx, ny = x + dx, y + dy

            if (nx, ny) == obstruction or (0 <= nx < len(grid) and 0 <= ny < len(grid) and grid[nx][ny] == '#'):
                direction_idx = (direction_idx + 1) % 4  # Turn right
            else:
                x, y = nx, ny
                if (x, y) in visited:
                    return True
                if not (0 <= x < len(grid) and 0 <= y < len(grid)):
                    break
                visited.add((x, y))

        return False

    loop_positions = []
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] == '.' and (i, j) != start_pos:
                if simulate_with_obstruction((i, j)):
                    loop_positions.append((i, j))

    return len(loop_positions)