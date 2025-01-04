

def check(input_array, x, y):
    if (input_array[x][y] != 1):
        return
    else:
        global score 
        score += 1
        if (x + 1) < len(input_array):
            check(input_array, x + 1, y)
        if (y + 1) < len (input_array[x]):
            check(input_array, x, y + 1)
        if ((x + 1) < len(input_array)) and ((y + 1) < len (input_array[x])):
            check(input_array, x + 1, y + 1)
        return

array_1 = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
array_2 = [[0,0,0,1],[0,0,0,1],[0,0,0,1],[0,0,0,1]]
array_3 = [[1,1,1,1],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

score = array_1
for i in range(4):
    for j in range(4):
        score[i][j] = {
            'up': 0,
            'up-right': 0,
            'right': 0,
            'down-right': 0,
            'down': 0,
            'down-left': 0,
            'left': 0,
            'up-left': 0
        }


count = 0
score = 0

for i in range(4):
    for j in range (4):
        check(array_2, i, j)
        count += 1

print(count)
print(score)