with open('day-05/input1') as file:
    data = [i for i in file.read().strip().split("\n")]

crates = [
    ['T', 'P', 'Z', 'C', 'S', 'L', 'Q', 'N'],
    ['L', 'P', 'T', 'V', 'H', 'C', 'G'],
    ['D', 'C', 'Z', 'F'],
    ['G', 'W', 'T', 'D', 'L', 'M', 'V', 'C'],
    ['P', 'W', 'C'],
    ['P', 'F', 'J', 'D', 'C', 'T', 'S', 'Z'],
    ['V', 'W', 'G', 'B', 'D'],
    ['N', 'J', 'S', 'Q', 'H', 'W'],
    ['R', 'C', 'Q', 'F', 'S', 'L', 'V']
]

for item in data:
    crane = [int(s) for s in item.split() if s.isdigit()]
    index = crane[0]
    colfrom = crane[1] - 1
    colto  = crane[2] - 1
    while index != 0:
        moved = crates[colfrom].pop()
        crates[colto].append(moved)
        index -= 1
print(crates)
print('回答は',crates[0].pop(),crates[1].pop(),crates[2].pop(),crates[3].pop(),crates[4].pop(),crates[5].pop(),crates[6].pop(),crates[7].pop(),crates[8].pop())