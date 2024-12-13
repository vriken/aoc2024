with open('/Users/akeros/Downloads/input.txt', 'r') as file:
    data = file.read().strip()

def parse_disk_map(disk_map):
    blocks = []
    file_id = 0
    is_file = True

    for length in map(int, disk_map):
        if is_file:
            blocks.extend([file_id] * length)
            file_id += 1
        else:
            blocks.extend([-1] * length)
        is_file = not is_file

    return blocks

def move_blocks(blocks):
    for i in range(len(blocks) - 1, -1, -1):
        if blocks[i] != -1:
            for j in range(i):
                if blocks[j] == -1:
                    blocks[j], blocks[i] = blocks[i], -1
                    break
    return blocks

def move_files(blocks):
    max_file_id = max(blocks)
    for file_id in range(max_file_id, -1, -1):
        file_positions = [i for i, block in enumerate(blocks) if block == file_id]
        if not file_positions:
            continue

        file_size = len(file_positions)

        for i in range(len(blocks) - file_size + 1):
            if all(block == -1 for block in blocks[i:i + file_size]):

                for pos in file_positions:
                    blocks[pos] = -1
                for j in range(file_size):
                    blocks[i + j] = file_id
                break

    return blocks

def calculate_checksum(blocks):
    checksum = 0
    for position, block in enumerate(blocks):
        if block != -1:
            checksum += position * block
    return checksum

def main(disk_map):
    parsed_blocks = parse_disk_map(disk_map)
    # compacted_blocks = move_blocks(parsed_blocks)
    compacted_blocks = move_files(parsed_blocks)
    checksum = calculate_checksum(compacted_blocks)
    return checksum

result = main(data)
print("Checksum:", result)
