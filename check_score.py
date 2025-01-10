

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

new_array = [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]

'''
  A B C D E F G
1
2
3
4
5
6

'''




# 6 rows, 7 columns - arrays within arrays are columns within rows

score_row = [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]       # starts at A1-D1
score_column = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]    # starts at A1-A4
score_diagonal_up_right = [[0,0,0],[0,0,0],[0,0,0],[0,0,0]]                 # starts at A4-D1
score_diagonal_down_right = [[0,0,0],[0,0,0],[0,0,0],[0,0,0]]               # starts at A1-D4

i = 6
j = 7

# populate score_row

for col_num in range((j - 4) + 1):
    for row_num in range(i):
        score_row[col_num][row_num] = {
            'A': 0,
            'B': 0,
            'Score': 0
        }


# populate score_column

for col_num in range(j):
    for row_num in range((i - 4) + 1):
        score_column[col_num][row_num] = {
            'A': 0,
            'B': 0,
            'Score': 0
        }


# populate score_diagonal_up_right

for col_num in range((j - 4) + 1):
    for row_num in range((i - 4) + 1):
        score_diagonal_up_right[col_num][row_num] = {
            'A': 0,
            'B': 0,
            'Score': 0
        }


# populate score_diagonal_down_right

for col_num in range((j - 4) + 1):
    for row_num in range((i - 4) + 1):
        score_diagonal_up_right[col_num][row_num] = {
            'A': 0,
            'B': 0,
            'Score': 0
        }






'''
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
'''

count = 0
score = 0

for i in range(4):
    for j in range (4):
        check(array_2, i, j)
        count += 1

print(count)
print(score)