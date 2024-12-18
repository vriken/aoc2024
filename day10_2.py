with open('/Users/akeros/Downloads/input.txt', 'r') as file:
    data = file.read().strip().split('\n')

def find_trailheads(grid):
    rows, cols = len(grid), len(grid[0])
    trailheads = []

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 0:
                trailheads.append((i, j))
    return trailheads

def get_valid_moves(pos, grid, current_height):
    rows, cols = len(grid), len(grid[0])
    i, j = pos
    moves = []
    
    directions = [(0,1), (0,-1), (1,0), (-1,0)]
    for di, dj in directions:
        ni, nj = i + di, j + dj
        if (0 <= ni < rows and 0 <= nj < cols and 
            grid[ni][nj] == current_height + 1):
            moves.append((ni, nj))
    return moves

def count_distinct_paths(start, grid):
    paths = set()
    current_path = []
    
    def dfs(pos, height):
        if height == 9:
            paths.add(tuple(current_path))
            return
        
        for next_pos in get_valid_moves(pos, grid, height):
            current_path.append(next_pos)
            dfs(next_pos, height + 1)
            current_path.pop()
    
    current_path.append(start)
    dfs(start, 0)
    return len(paths)

def solve(grid):
    trailheads = find_trailheads(grid)
    total_rating = 0
    
    for trailhead in trailheads:
        rating = count_distinct_paths(trailhead, grid)
        total_rating += rating
    
    return total_rating

grid = [[int(char) for char in line] for line in data]
print(solve(grid))
