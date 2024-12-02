import numpy as np
def is_safe_with_dampener(sequence):
    diffs = np.diff(sequence)
    if (np.all(diffs > 0) or np.all(diffs < 0)) and np.all(np.abs(diffs) >= 1) and np.all(np.abs(diffs) <= 3):
        return True
    
    for i in range(len(sequence)):
        temp_sequence = sequence[:i] + sequence[i+1:]
        diffs = np.diff(temp_sequence)
        if (np.all(diffs > 0) or np.all(diffs < 0)) and np.all(np.abs(diffs) >= 1) and np.all(np.abs(diffs) <= 3):
            return True
    return False

with open('C:\\Users\\vrike\\Downloads\\input.txt', 'r') as file:
    sequences = [[int(x) for x in line.strip().split()] for line in file.readlines()]

safe_count = sum(1 for seq in sequences if is_safe_with_dampener(seq))
print(safe_count)