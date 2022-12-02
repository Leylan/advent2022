with open('day-01/input1') as file:
    data = [i for i in file.read().strip().split("\n")]

print(data)

max = 0
count = 0
for item in data:
        if item == '':
            count = 0
        else:
            num = int(item)
            count += num
        
        if count > max:
            max = count

print(max)