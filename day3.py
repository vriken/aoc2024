with open('C:\\Users\\vrike\\Downloads\\input.txt', 'r') as file:
    data = file.read()

import re
on = True
operations = re.findall(r"don't\(\)|do\(\)|mul\(\d+,\d+\)", data)

results = []
for x in operations:
    val = 0
    if x == "don't()":
        on = False
    elif x == "do()":
        on = True
    else:
        numbers = [int(n) for n in re.findall(r'\d+', x)]
        val = numbers[0] * numbers[1]
    
    results.append([val, val] if on else [val, 0])

final_result = [sum(col) for col in zip(*results)]
print(final_result[0])