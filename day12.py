import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from scipy.ndimage import label

with open('/Users/akeros/Downloads/input.txt', 'r') as file:
    data = file.read().strip()

def calculate_perimeter(region_mask):
    rows, cols = region_mask.shape
    perimeter = 0
    directions = [(0,1), (0,-1), (1,0), (-1,0)]
    
    for i in range(rows):
        for j in range(cols):
            if region_mask[i,j]:
                # Count exposed edges
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if (ni < 0 or ni >= rows or 
                        nj < 0 or nj >= cols or 
                        not region_mask[ni,nj]):
                        perimeter += 1
    return perimeter

def calculate_region_stats(garden_str):
    garden = np.array([list(line) for line in garden_str.splitlines() if line])
    unique_chars = np.unique(garden)
    total_cost = 0
    
    fig, ax = plt.subplots(figsize=(30, 30))
    colors = plt.cm.Set3(np.linspace(0, 1, len(unique_chars)))
    color_dict = {char: color for char, color in zip(unique_chars, colors)}
    
    for char in unique_chars:
        mask = (garden == char)
        labeled, num_regions = label(mask)
        
        for region_id in range(1, num_regions + 1):
            region_mask = (labeled == region_id)
            area = np.sum(region_mask)
            perimeter = calculate_perimeter(region_mask)
            cost = area * perimeter
            total_cost += cost
            
            # Visualization
            for i in range(garden.shape[0]):
                for j in range(garden.shape[1]):
                    if region_mask[i,j]:
                        ax.add_patch(Rectangle((j, garden.shape[0]-i-1), 1, 1,
                                            facecolor=color_dict[char],
                                            edgecolor='black',
                                            alpha=0.7))
                        ax.text(j+0.5, garden.shape[0]-i-0.5, char,
                               ha='center', va='center', fontsize=6)
    
    ax.set_xlim(-0.5, garden.shape[1]+0.5)
    ax.set_ylim(-0.5, garden.shape[0]+0.5)
    ax.grid(True, linewidth=0.2, alpha = 0.5)
    plt.rcParams.update({'font.size': 8})
    plt.title(f'Total Cost: {total_cost}')
    plt.show()
    
    return total_cost

total_cost = calculate_region_stats(data)
print(f"Total cost of all regions: {total_cost}")
