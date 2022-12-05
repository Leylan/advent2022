with open('day-04/input1') as file:
    data = [i for i in file.read().strip().split("\n")]

count = 0
for item in data:
    firstelf = list(item.split(',')[0].split('-'))
    secondelf = list(item.split(',')[1].split('-'))
    rangefirst = set(range(int(firstelf[0]), int(firstelf[1])+1))
    rangesecond = set(range(int(secondelf[0]), int(secondelf[1])+1))
    if (rangefirst.intersection(rangesecond)):
        count += 1

print ('オバーラップしているのは数',count,'です')
    