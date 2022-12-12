import collections

with open('day-12/input1') as file:
    data = [ list( l.strip( '\n' ) ) for l in file ]

width, height = len(data[0]), len(data)

queue = collections.deque()
pos = {}

#スタートとフィニッシュを見つけるため
for y, r in enumerate(data):
    for x, c in enumerate(r):
        if c in ("S", "a"):
            queue.append((x, y))
            pos[(x, y)] = 0
            data[y][x] = "a"
        elif c == "E":
            ex, ey = x, y
            data[y][x] = "z"

while queue:
    x, y = queue.popleft()
    if (x, y) == (ex, ey):
        break
    for nx, ny in ((x,  y-1), (x+1, y), (x, y+1), (x-1, y)):
        if (0 <= nx < width and 0 <= ny < height and (nx, ny) not in pos and
            ord(data[ny][nx]) - ord( data[y][x]) <= 1):
            queue.append((nx, ny))
            pos[(nx, ny)] = pos[(x, y)] + 1
print(pos[ex, ey])