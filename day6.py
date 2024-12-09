with open('C:\\Users\\vrike\\Downloads\\input.txt', 'r') as file:
    data = file.read().strip().split('\n')

def simulate_guard_movement(grid):
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

    visited = set()
    x, y = start_pos
    visited.add((x, y))

    while 0 <= x < len(grid) and 0 <= y < len(grid):
        dx, dy = directions[direction_index]
        nx, ny = x + dx, y + dy

        if 0 <= nx < len(grid) and 0 <= ny < len(grid) and grid[nx][ny] == '#':
            direction_index = (direction_index + 1) % 4  # Turn right
        else:
            x, y = nx, ny
            if not (0 <= x < len(grid) and 0 <= y < len(grid)):
                break
            visited.add((x, y))

    return len(visited)

if __name__ == '__main__':
    print(simulate_guard_movement(data))