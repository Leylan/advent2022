with open('day-02/input2') as file:
    data = [i for i in file.read().strip().split("\n")]

# Rock AX Paper BY Cissors CZ
point = 0
for item in data:
    list(item)
    if item[2] == "X":
        point += 0
        if item[0] == "A":
            point += 3
        if item[0] == "B":
            point += 1
        if item[0] == "C":
            point += 2
    if item[2] == "Y":
        point += 3
        if item[0] == "A":
            point += 1
        if item[0] == "B":
            point += 2
        if item[0] == "C":
            point += 3
    if item[2] == "Z":
        point += 6
        if item[0] == "A":
            point += 2
        if item[0] == "B":
            point += 3
        if item[0] == "C":
            point += 1

print('じゃんけんで',point,'貯めた')