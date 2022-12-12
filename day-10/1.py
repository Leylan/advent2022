with open('day-10/input1') as file:
    data = [i for i in file.read().strip().split("\n")]

X = 1
cycles = 0
signal_strengths = {}

for inst in data:
    match inst.split()[0]:
        case "noop":
            cycles += 1
            signal_strengths[cycles] = X * cycles
        case "addx":
            cycles += 1
            signal_strengths[cycles] = X * cycles
            
            cycles += 1
            signal_strengths[cycles] = X * cycles
            X += int(inst.split()[1])

print (signal_strengths)
sumr = sum(signal_strengths.get(i, 0) for i in range(20, 221, 40))
print(sumr)