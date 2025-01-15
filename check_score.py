
'''
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
'''


new_array = [[0,0,'A','A','A','A'],[0,0,0,'B','A','A'],[0,0,0,'A','A','A'],[0,0,0,0,0,0],[0,0,0,0,'A','A'],[0,0,0,0,0,0],[0,0,0,0,0,0]]



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
        score_diagonal_down_right[col_num][row_num] = {
            'A': 0,
            'B': 0,
            'Score': 0
        }


def check_columns(array):
    for j in range(len(array)):
        for i in range((len(array[j]) - 3)):
            for z in range(4):
                if array[j][i + z] == 'A':
                    score_column[j][i]['A'] += 1
                elif array[j][i + z] == 'B':
                    score_column[j][i]['B'] += 1
            if score_column[j][i]['A'] != 0 and score_column[j][i]['B'] != 0:
                score_column[j][i]['Score'] = 'X'
            else:
                score_column[j][i]['Score'] = score_column[j][i]['A'] - score_column[j][i]['B']


def check_rows(array):
    for j in range(len(array) - 3):
        for i in range(len(array[j])):
            for z in range(4):
                if array[j + z][i] == 'A':
                    score_row[j][i]['A'] += 1
                elif array[j + z][i ] == 'B':
                    score_row[j][i]['B'] += 1
            if score_row[j][i]['A'] != 0 and score_row[j][i]['B'] != 0:
                score_row[j][i]['Score'] = 'X'
            else:
                score_row[j][i]['Score'] = score_row[j][i]['A'] - score_row[j][i]['B']


def check_diagonals_up_right(array):
    for j in range(len(array) - 3):
        for i in range(len(array[j]) - 3):
            for z in range(4):
                # print('i = ', i,', j = ', j, ', z = ', z)
                # print('Value is ', array[j + z][i + 3 - z])
                if array[j + z][i + 3 - z] == 'A':
                    score_diagonal_up_right[j][i]['A'] += 1
                elif array[j + z][i + 3 - z] == 'B':
                    score_diagonal_up_right[j][i]['B'] += 1
                # print(score_diagonal_up_right[j][i]['A'])
            if score_diagonal_up_right[j][i]['A'] != 0 and score_diagonal_up_right[j][i]['B'] != 0:
                score_diagonal_up_right[j][i]['Score'] = 'X'
            else:
                score_diagonal_up_right[j][i]['Score'] = score_diagonal_up_right[j][i]['A'] - score_diagonal_up_right[j][i]['B']


def check_diagonals_down_right(array):
    for j in range(len(array) - 3):
        for i in range(len(array[j]) - 3):
            for z in range(4):
                if array[j + z][i + z] == 'A':
                    score_diagonal_down_right[j][i]['A'] += 1
                elif array[j + z][i + z] == 'B':
                    score_diagonal_down_right[j][i]['B'] += 1
                # print(score_diagonal_down_right[j][i]['A'])
            if score_diagonal_down_right[j][i]['A'] != 0 and score_diagonal_down_right[j][i]['B'] != 0:
                score_diagonal_down_right[j][i]['Score'] = 'X'
            else:
                score_diagonal_down_right[j][i]['Score'] = score_diagonal_down_right[j][i]['A'] - score_diagonal_down_right[j][i]['B']


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

# print(new_array)
# check_columns(new_array)
# check_rows(new_array)
# check_diagonals_up_right(new_array)
# check_diagonals_down_right(new_array)
# print(score_column)

# 6 rows by 7 columns

i = 6
j = 7

dummy_array = [[0 for x in range(i)] for y in range(j)]
dummy_score_row = [[0 for x in range(len(dummy_array[0]))] for y in range(len(dummy_array) - 3)]
dummy_score_column = [[0 for x in range(len(dummy_array[0]) - 3)] for y in range(len(dummy_array))]
dummy_score_diagonal_left = [[0 for x in range(len(dummy_array[0]) - 3)] for y in range(len(dummy_array) - 3)]
dummy_score_diagonal_right = [[0 for x in range(len(dummy_array[0]) - 3)] for y in range(len(dummy_array) - 3)]

print(dummy_score_diagonal_right)