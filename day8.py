with open('/Users/akeros/Downloads/input.txt', 'r') as input_file:
    data = [line.strip() for line in input_file if line.strip()]

height, width = len(data), len(data[0])

class Coordinate:
    def __init__(self, frequency, is_antinode, x, y):
        self.frequency = frequency
        self.is_antinode = is_antinode
        self.x = x
        self.y = y

def print_map(coords):
    for row in coords:
        print("".join('#' if cell.is_antinode else cell.frequency for cell in row))

def count_antinodes(coords):
    return sum(cell.is_antinode for row in coords for cell in row)

def set_antinodes(coords, x, y, dx, dy):
    nx, ny = x - dx, y - dy
    if 0 <= nx < height and 0 <= ny < width:
        coords[nx][ny].is_antinode = True
        return True
    return False

def p1(coords, tracker):
    for antennas in tracker.values():
        for a in antennas:
            for b in antennas:
                if a != b:
                    dx, dy = b.x - a.x, b.y - a.y
                    set_antinodes(coords, a.x, a.y, dx, dy)
                    set_antinodes(coords, b.x, b.y, -dx, -dy)
    return count_antinodes(coords)

def p2(coords, tracker):
    for antennas in tracker.values():
        for a in antennas:
            coords[a.x][a.y].is_antinode = True
            for b in antennas:
                if a != b:
                    dx, dy = b.x - a.x, b.y - a.y
                    
                    i = 1
                    while set_antinodes(coords, a.x, a.y, dx * i, dy * i):
                        i += 1
                    i = 1
                    while set_antinodes(coords, a.x, a.y, -dx * i, -dy * i):
                        i += 1

    return count_antinodes(coords)

def main():
    coords = [[Coordinate(data[i][j], False, i, j) for j in range(width)] for i in range(height)]
    tracker = {}

    for i in range(height):
        for j in range(width):
            char = data[i][j]
            if char != '.':
                tracker.setdefault(char, []).append(coords[i][j])
    
    print(p1(coords, tracker))
    
    coords = [[Coordinate(data[i][j], False, i, j) for j in range(width)] for i in range(height)]
    print(p2(coords, tracker))

if __name__ == "__main__":
    main()
