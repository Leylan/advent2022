with open('day-03/input1') as file:
    data = [i for i in file.read().strip().split("\n")]

total = 0
for item in data:
    wordlen = len(item)//2
    firstword = item[0:wordlen]
    secondword = item[wordlen:wordlen*2]
    lst = list(set(firstword)&set(secondword))
    commonletter = lst[0]
    if commonletter.isupper():
        value = ord(commonletter)-38
    elif commonletter.islower():
        value = ord(commonletter)-96
    
    total += value
    
print('優先度合計は',total)

