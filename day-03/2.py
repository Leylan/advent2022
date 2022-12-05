with open('day-03/input2') as file:
    data = [i for i in file.read().strip().split("\n")]

count = 0
total = 0
commonletterlist = []
for item in data:
    count += 1
    match count:
        case 1:
            w1 = item
        case 2:
            w2 = item
        case 3:
            w3 = item
        
    if count == 3:
        lst = list(set(w1)&set(w2)&set(w3))
        commonletter = lst[0]
        if commonletter.isupper():
            value = ord(commonletter)-38
        elif commonletter.islower():
            value = ord(commonletter)-96
        count = 0
        commonletterlist.clear()
        total += value

print('優先度合計は',total)

