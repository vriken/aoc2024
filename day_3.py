with open('C:\\Users\\vrike\\Downloads\\input.txt', 'r') as file:
    data = file.read()

import re

is_counting_enabled = True
commands = re.findall(r"don't\(\)|do\(\)|mul\(\d+,\d+\)", data)

all_calculations = []

for command in commands:
    result = 0
    
    if command == "don't()":
        is_counting_enabled = False
    
    elif command == "do()":
        is_counting_enabled = True
    
    else:
        numbers = re.findall(r'\d+', command)
        first_number = int(numbers[0])
        second_number = int(numbers[1])
        
        result = first_number * second_number

    if is_counting_enabled:
        all_calculations.append([result, result])
    else:
        all_calculations.append([result, 0])

totals = [sum(column) for column in zip(*all_calculations)]
print(totals[0])
