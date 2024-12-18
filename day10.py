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

def count_reachable_nines(start, grid):
    visited = set()
    reachable_nines = set()
    
    def dfs(pos, height):
        if height == 9:
            reachable_nines.add(pos)
            return
        
        visited.add(pos)
        for next_pos in get_valid_moves(pos, grid, height):
            if next_pos not in visited:
                dfs(next_pos, height + 1)
        visited.remove(pos)
    
    dfs(start, 0)
    return len(reachable_nines)

def solve(grid):
    trailheads = find_trailheads(grid)
    total_score = 0
    
    for trailhead in trailheads:
        score = count_reachable_nines(trailhead, grid)
        total_score += score
    
    return total_score

grid = [[int(char) for char in line] for line in data]
print(solve(grid))
