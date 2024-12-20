import multiprocessing as mp
import numpy as np
from collections import Counter

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

def process_chunk(stones_with_counts):
    result = Counter()
    for stone, count in stones_with_counts.items():
        new_stones = transform_stone(stone)
        for new_stone in new_stones:
            result[new_stone] += count
    return result

def simulate_blinks(stones, blinks):
    current_stones = Counter(stones)
    num_cores = mp.cpu_count()
    
    for _ in range(blinks):
        items = list(current_stones.items())
        chunk_size = max(1, len(items) // num_cores)
        chunks = [dict(items[i:i + chunk_size]) 
                 for i in range(0, len(items), chunk_size)]
        
        with mp.Pool(num_cores) as pool:
            results = pool.map(process_chunk, chunks)
        
        current_stones = sum(results, Counter())

    return sum(current_stones.values())

def solve(input):
    initial_stones = [int(x) for x in input]
    return simulate_blinks(initial_stones, 75)

if __name__ == '__main__':
    print(solve(data))
