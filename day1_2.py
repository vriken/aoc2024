with open('C:\\Users\\vrike\\Downloads\\input.txt', 'r') as file:
    data = file.read()

left_list = []
right_list = []
    
for line in data.strip().split('\n'):
    if line:
        left, right = map(int, line.split())
        left_list.append(left)
        right_list.append(right)
    
right_freq = {}
for num in right_list:
    right_freq[num] = right_freq.get(num, 0) + 1
    
total_score = 0
for num in left_list:
    total_score += num * right_freq.get(num, 0)

print(total_score)