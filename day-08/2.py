import numpy as np

with open('day-08/input1') as file:
    data = [i for i in file.read().strip().split("\n")]

grid = np.array([list(x.strip()) for x in data], int)
scenic = np.ones_like(grid, int)

for _ in range(4):
    for x,y in np.ndindex(grid.shape):   
        lower = [t < grid[x,y] for t in grid[x,y+1:]]
        scenic[x,y] *= next((i+1 for i,t in enumerate(lower) if ~t), len(lower))
    grid, scenic = map(np.rot90,[grid, scenic])
print(scenic.max())