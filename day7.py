with open('C:\\Users\\vrike\\Downloads\\input.txt', 'r') as file:
    data = file.read().strip().split('\n')

def evaluate_expression(numbers, operators):
    result = numbers[0]
    for i in range(len(operators)):
        if operators[i] == '+':
            result += numbers[i + 1]
        elif operators[i] == '*':
            result *= numbers[i + 1]
        elif operators[i] == '||':
            result = int(str(result) + str(numbers[i + 1]))
    return result

def generate_operator_combinations(num_operators):
    from itertools import product
    return list(product(['+', '*', '||'], repeat=num_operators))

def calculate_calibration_result(input_data):
    total_result = 0

    for line in input_data:
        target, numbers = line.split(':')
        target = int(target.strip())
        numbers = list(map(int, numbers.strip().split()))

        num_operators = len(numbers) - 1
        operator_combinations = generate_operator_combinations(num_operators)

        valid = False
        for operators in operator_combinations:
            if evaluate_expression(numbers, operators) == target:
                valid = True
                break

        if valid:
            total_result += target

    return total_result

total_calibration_result = calculate_calibration_result(data)
print(total_calibration_result)
