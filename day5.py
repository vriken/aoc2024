with open('C:\\Users\\vrike\\Downloads\\input.txt', 'r') as file:
    input_data = file.read()

def parse_input(input_str):
    sections = input_str.strip().split('\n\n')
    rules_section = sections[0].split('\n')
    updates_section = sections[1].split('\n')
    
    rules = [tuple(map(int, rule.split('|'))) for rule in rules_section]
    updates = [list(map(int, update.split(','))) for update in updates_section]
    
    return rules, updates

def is_correct_order(update, rules):
    for X, Y in rules:
        if X in update and Y in update:
            if update.index(X) > update.index(Y):
                return False
    return True

def find_middle_page(update):
    return update[len(update) // 2]

def correct_order(update, rules):
    update_set = set(update)
    graph = {page: [] for page in update}
    in_degree = {page: 0 for page in update}
    
    for x, y in rules:
        if x in update_set and y in update_set:
            graph[x].append(y)
            in_degree[y] += 1
    
    queue = [page for page in update if in_degree[page] == 0]
    sorted_update = []
    
    while queue:
        current = queue.pop(0)
        sorted_update.append(current)
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    return sorted_update

def main(input_str):
    rules, updates = parse_input(input_str)
    
    correct_updates = []
    incorrect_updates = []
    
    for update in updates:
        if is_correct_order(update, rules):
            correct_updates.append(update)
        else:
            incorrect_updates.append(update)
    
    correct_middle_pages = [find_middle_page(update) for update in correct_updates]
    corrected_middle_pages = [find_middle_page(correct_order(update, rules)) for update in incorrect_updates]
    
    return sum(correct_middle_pages), sum(corrected_middle_pages)

correct_sum, corrected_sum = main(input_data)

print("Sum of middle pages of correct updates:", correct_sum)
print("Sum of middle pages of corrected updates:", corrected_sum)