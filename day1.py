with open('C:\\Users\\vrike\\Downloads\\input.txt', 'r') as file:
    data = file.read()

left_list = []
right_list = []

for line in data.strip().split('\n'):
    if line:
        left, right = map(int, line.split())
        left_list.append(left)
        right_list.append(right)
    
left_list.sort()
right_list.sort()    
total_distance = 0
for l, r in zip(left_list, right_list):
    distance = abs(l - r)
    total_distance += distance
        
print(total_distance)