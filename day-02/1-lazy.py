with open('day-02/input2') as file:
    data = [i for i in file.read().strip().split("\n")]

# Rock AX Paper BY Cissors CZ
point = 0
for item in data:
    match item:
        case 'A X':
            point += 4
        case 'A Y':
            point += 8
        case 'A Z':
            point += 3
        case 'B X':
            point += 1
        case 'B Y':
            point += 5
        case 'B Z':
            point += 9
        case 'C X':
            point += 7
        case 'C Y':
            point += 2
        case 'C Z':
            point += 6

print('じゃんけんで',point,'貯めた')