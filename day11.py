with open('/Users/akeros/Downloads/input.txt', 'r') as file:
    data = file.read().strip().split()

def transform_stone(stone):
    if stone == 0:
        return [1]
    
    stone_str = str(stone)

    if len(stone_str) % 2 == 0:
        mid = len(stone_str) // 2
        left = int(stone_str[:mid])
        right = int(stone_str[mid:])
        return [left, right]
    
    return [stone * 2024]

def simulate_blinks(stones, blinks):
    current_stones = stones[:]

    for _ in range(blinks):
        new_stones = []
        for stone in current_stones:
            new_stones.extend(transform_stone(stone))
        current_stones = new_stones

    return len(current_stones)

def solve(input):
    initial_stones = [int(x) for x in input]
    return simulate_blinks(initial_stones, 25)

print(solve(data))

