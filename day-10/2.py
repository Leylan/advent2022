with open('day-10/input1') as file:
    data = [i for i in file.read().strip().split("\n")]

X = 1
cycles = 0
pixels = list("." * 40 * 6)

def update_pixels(X, cycles, pixels):
	pos = (cycles - 1) % 40
	if pos in {X-1, X, X+1}:
		pixels[cycles - 1] = "#"

for inst in data:
    match inst.split()[0]:
        case "noop":
            cycles += 1
            update_pixels(X, cycles, pixels)
        case "addx":
            cycles += 1
            update_pixels(X, cycles, pixels)
            
            cycles += 1
            update_pixels(X, cycles, pixels)
            X += int(inst.split()[1])

for i in range(0, 201, 40):
	print("".join(pixels[i: i + 40]))