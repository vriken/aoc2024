with open('C:\\Users\\vrike\\Downloads\\input.txt', 'r') as file:
    data = file.read().strip().split('\n')


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

def simulate_guard_movement():
    current_position = start_position.copy()
    visited_positions = set()
    
    while True:
        x, y, direction = current_position['x'], current_position['y'], current_position['direction']
        visited_positions.add(f"{x},{y}")
        
        dx, dy = directions[direction]['dx'], directions[direction]['dy']
        next_x, next_y = x + dx, y + dy
        
        if next_x < 0 or next_x >= len(data) or next_y < 0 or next_y >= len(data[0]):
            break
        
        if data[next_x][next_y] == '#':
            current_position = {'x': x, 'y': y, 'direction': turn_right(direction)}
        else:
            current_position = {'x': next_x, 'y': next_y, 'direction': direction}
    
    return {'visited_positions': visited_positions}

if __name__ == '__main__':
    result = simulate_guard_movement()
    print("Total visited positions:", len(result['visited_positions']))