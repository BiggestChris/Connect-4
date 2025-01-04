from tabulate import tabulate

print(tabulate([['x',1,2,3],[1,0,0,0],[2,0,0,0],[3,0,0,0]], tablefmt="grid", colalign=("center","center")))