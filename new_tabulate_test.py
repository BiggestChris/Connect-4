from tabulate import tabulate

print(tabulate([['x',1,2,3],[1,0,0,0],[2,0,0,0],[3,0,0,0]], tablefmt="grid", colalign=("center","center")))

grid = [['x',1,2,3,4,5,6],[1,0,0,0,0,0,0],[2,0,0,0,0,0,0],[3,0,0,0,0,0,0],[4,0,0,0,0,0,0],[5,0,0,0,0,0,0],[6,0,0,0,0,0,0],[7,0,0,0,0,0,0]]

transposed_grid = list(map(list, zip(*grid)))

print(tabulate(transposed_grid, tablefmt="grid", colalign=("center","center")))