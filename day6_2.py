with open('C:\\Users\\vrike\\Downloads\\input.txt', 'r') as file:
    data = [list(row) for row in file.read().strip().split('\n')]


directions = {
    'U': {'dx': -1, 'dy': 0},
    'D': {'dx': 1, 'dy': 0},
    'L': {'dx': 0, 'dy': -1},
    'R': {'dx': 0, 'dy': 1}
}

def turn_right(direction):
    if direction == 'U':
        return 'R'
    if direction == 'D':
        return 'L'
    if direction == 'L':
        return 'U'
    if direction == 'R':
        return 'D'

def find_start_position():
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == '^':
                data[i] = list(data[i])
                data[i][j] = '.'
                data[i] = ''.join(data[i])
                return {'x': i, 'y': j, 'direction': 'U'}


start_position = find_start_position()

def simulate_guard_movement(grid):
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # Up, Right, Down, Left
    direction_index = 0
    start_pos = None

    # Find starting position and direction
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

    # Raise an error if no starting position is found
    if start_pos is None:
        raise ValueError("No starting position found in the grid. Ensure the input contains '^', '>', 'v', or '<'.")

    visited = set()
    x, y = start_pos
    visited.add(f"{x},{y}")

    while 0 <= x < len(grid) and 0 <= y < len(grid[0]):
        dx, dy = directions[direction_index]
        nx, ny = x + dx, y + dy

        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == '#':
            direction_index = (direction_index + 1) % 4  # Turn right
        else:
            x, y = nx, ny
            if not (0 <= x < len(grid) and 0 <= y < len(grid[0])):
                break
            visited.add(f"{x},{y}")

    return {'visited_positions': visited}



def simulate_with_obstruction():
    current_position = start_position.copy()
    visited_states = set()
    
    while True:
        x, y, direction = current_position['x'], current_position['y'], current_position['direction']
        
        if f"{x},{y},{direction}" in visited_states:
            return True
        
        visited_states.add(f"{x},{y},{direction}")
        
        dx, dy = directions[direction]['dx'], directions[direction]['dy']
        next_x, next_y = x + dx, y + dy
        
        if next_x < 0 or next_x >= len(data) or next_y < 0 or next_y >= len(data[0]):
            break
        
        if data[next_x][next_y] == '#':
            current_position = {'x': x, 'y': y, 'direction': turn_right(direction)}
        else:
            current_position = {'x': next_x, 'y': next_y, 'direction': direction}
    
    return False

def part2():
    result_part1 = simulate_guard_movement(data)
    visited_positions_list = [
        {'x': int(x), 'y': int(y)}
        for position in result_part1['visited_positions']
        for x, y in [position.split(',')]
    ]
    
    loop_count = 0
    
    for position in visited_positions_list:
        x, y = position['x'], position['y']
        
        if x == start_position['x'] and y == start_position['y']:
            continue
        
        data[x] = list(data[x])
        data[x][y] = '#'
        
        if simulate_with_obstruction():
            loop_count += 1
        
        data[x][y] = '.'
        data[x] = ''.join(data[x])
    
    return loop_count


if __name__ == '__main__':
    print(part2())
