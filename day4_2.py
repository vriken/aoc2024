import matplotlib.pyplot as plt
import numpy as np

# Read the file
with open('C:\\Users\\vrike\\Downloads\\input.txt', 'r') as file:
    data = file.read().strip().split('\n')

def find_xmas_patterns(grid):
    rows = len(grid)
    cols = len(grid[0])
    count = 0
    pattern_coords = []
    
    def is_mas(chars):
        return ''.join(chars) in ['MAS', 'SAM']
    
    for row in range(1, rows-1):
        for col in range(1, cols-1):
            if grid[row][col] != 'A':
                continue
                
            tlbr = [grid[row-1][col-1], grid[row][col], grid[row+1][col+1]]
            bltr = [grid[row+1][col-1], grid[row][col], grid[row-1][col+1]]
            
            if is_mas(tlbr) and is_mas(bltr):
                count += 1
                pattern_coords.append((row-1, col-1))
                pattern_coords.append((row, col))
                pattern_coords.append((row+1, col+1))
                pattern_coords.append((row+1, col-1))
                pattern_coords.append((row-1, col+1))
    
    return count, pattern_coords

result, pattern_coords = find_xmas_patterns(data)
print(result)

rows = len(data)
cols = len(data[0])
grid = np.zeros((rows, cols))

for (row, col) in pattern_coords:
    grid[row, col] = 1

plt.imshow(grid)
plt.show()