with open('day-02/input2') as file:
    data = [i for i in file.read().strip().split("\n")]

# Rock A Paper B Cissors C
# lose X draw Y win Z 
point = 0
for item in data:
    match item:
        case 'A X':
            point += 3
        case 'A Y':
            point += 4
        case 'A Z':
            point += 8
        case 'B X':
            point += 1
        case 'B Y':
            point += 5
        case 'B Z':
            point += 9
        case 'C X':
            point += 2
        case 'C Y':
            point += 6
        case 'C Z':
            point += 7

print('じゃんけんで',point,'貯めた')