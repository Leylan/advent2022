import numpy as np

with open('day-08/input1') as file:
    data = [i for i in file.read().strip().split("\n")]

grid = np.array([list(x.strip()) for x in data], int)
visible = np.zeros_like(grid, int)

for _ in range(4):
    for x,y in np.ndindex(grid.shape):   
        lower = [t < grid[x,y] for t in grid[x,y+1:]]
        visible[x,y] |= all(lower)
    grid, visible = map(np.rot90,[grid, visible])
print(visible.sum())