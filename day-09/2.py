with open('day-09/input1') as file:
    data = [i for i in file.read().strip().split("\n")]

visited = set([(0, 0)])
x, y = [0]*10, [0]*10
for item in data:
    direction, step = item.split()
    for i in range(int(step)):
        #頭を動かす
        x[0] += {"U": 0, "R": 1, "D": 0, "L": -1}[direction]
        y[0] += {"U": -1, "R": 0, "D": 1, "L": 0}[direction]
        for k in range(1, len(x)):
            #尻尾を動かす
            while (abs(x[k] - x[k-1]) > 1 or abs(y[k] - y[k-1]) > 1):
                x[k] += (x[k-1] > x[k]) - (x[k-1] < x[k])
                y[k] += (y[k-1] > y[k]) - (y[k-1] < y[k])
            visited.add((x[-1], y[-1]))
print("尻尾が留まった場所は",len(visited),"箇所です")