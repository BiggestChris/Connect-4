from tabulate import tabulate

class Board:
    # Initialise the object based on number of columns and rows
    def __init__(self, columns, rows):
        self.columns = columns
        self.rows = rows
        self._grid = self.__initialise_grid()
        self._score_row = self.__initialise_score_row()
        self._score_column = self.__initialise_score_column()
        self._score_diagonal_up_right = self.__initialise_score_diagonal_up_right()
        self._score_diagonal_down_right = self.__initialise_score_diagonal_down_right()
        
    def __str__(self):
        # Transpose the grid using zip and unpacking
        transposed_grid = list(map(list, zip(*self.grid)))
        return tabulate(transposed_grid, tablefmt="grid", colalign=("center","center"))


    def __initialise_grid(self):
        # Create the grid as an array of dimension equal to number of columns, each of those indices has an array of dimension equal to number of rows
        new_grid = []
        for number in range(self._columns):
            col = [0]
            for next_number in range(self._rows - 1):
                col.append(0)
            new_grid.append(col)
        return new_grid

    @property
    def grid(self):
        return self._grid

    @property
    def rows(self):
        return self._rows
    
    @rows.setter
    def rows(self, rows):
        try:
            rows = int(rows)
        except ValueError:
            raise ValueError("Number of rows must be integers")
        if (rows <= 0):
            raise ValueError("Rows must be greater than zero")
        elif (rows < 4):
            raise ValueError("Must be 4 or more rows")
        else:
            self._rows = rows
        
    @property
    def columns(self):
        return self._columns
    
    @columns.setter
    def columns(self, columns):
        try:
            columns = int(columns)
        except ValueError:
            raise ValueError("Number of columns must be integers")
        if (columns <= 0):
            raise ValueError("columns must be greater than zero")
        elif (columns < 4):
            raise ValueError("Must be 4 or more columns")
        else:
            self._columns = columns

    def add_coin(self, number, player):
        # print(self.grid[(number - 1)])
        for i in range(self.columns):
            if self.grid[(number - 1)][(-1 - i)] == 0:      # Will assume player treats game as one-indexed
                self._grid[(number - 1)][(-1 - i)] = player
                self._check_rows(self.grid)
                self._check_columns(self.grid)
                self._check_diagonals_down_right(self.grid)
                self._check_diagonals_up_right(self.grid)
                break
        # print(self.grid[(number - 1)])
        # TODO: Error handling so only 'A' or 'B' can be added
        # TODO: Control around adding when full

#TODO: Write in a function for two people to play the game (alternating turns)
#TODO: Write in an algorithm for an computer to play the game a virtual opponent
#TODO: Identify if someone has won the game
#TODO: Identify allowed/unallowed moves

    '''How to identify if someone has won the game
    '''

    @property
    def score_row(self):
        return self._score_row
    
    def __initialise_score_row(self):
        return [[{
            'A': 0, 
            'B': 0, 
            'Score': 0
            } for x in range(self._rows)] for y in range(self._columns - 3)]

    def _check_rows(self, array):
        for j in range(len(array) - 3):
            for i in range(len(array[j])):
                for z in range(4):
                    # print('j = ', j, 'i = ', i, 'z = ', z)
                    if array[j + z][i] == 'A':
                        self._score_row[j][i]['A'] += 1
                    elif array[j + z][i ] == 'B':
                        # print(self.score_row[j][0])
                        self._score_row[j][i]['B'] += 1
                if self._score_row[j][i]['A'] != 0 and self._score_row[j][i]['B'] != 0:
                    self._score_row[j][i]['Score'] = 'X'
                else:
                    self._score_row[j][i]['Score'] = self._score_row[j][i]['A'] - self._score_row[j][i]['B']


    @property
    def score_column(self):
        return self._score_column
    
    def __initialise_score_column(self):
        return [[{
            'A': 0, 
            'B': 0, 
            'Score': 0
            } for x in range(self._rows - 3)] for y in range(self._columns)]

    def _check_columns(self, array):
        for j in range(len(array)):
            for i in range(len(array[j]) - 3):
                for z in range(4):
                    # print('j = ', j, 'i = ', i, 'z = ', z)
                    if array[j][i + z] == 'A':
                        self._score_column[j][i]['A'] += 1
                    elif array[j][i + z] == 'B':
                        # print(self.score_column[j][0])
                        self._score_column[j][i]['B'] += 1
                if self._score_column[j][i]['A'] != 0 and self._score_column[j][i]['B'] != 0:
                    self._score_column[j][i]['Score'] = 'X'
                else:
                    self._score_column[j][i]['Score'] = self._score_column[j][i]['A'] - self._score_column[j][i]['B']


    @property
    def score_diagonal_up_right(self):
        return self._score_diagonal_up_right
    
    def __initialise_score_diagonal_up_right(self):
        return [[{
            'A': 0, 
            'B': 0, 
            'Score': 0
            } for x in range(self._rows - 3)] for y in range(self._columns - 3)]

    def _check_diagonals_up_right(self, array):
        for j in range(len(array) - 3):
            for i in range(len(array[j]) - 3):
                for z in range(4):
                    # print('j = ', j, 'i = ', i, 'z = ', z)
                    if array[j + z][i + 3 - z] == 'A':
                        self._score_diagonal_up_right[j][i]['A'] += 1
                    elif array[j + z][i + 3 - z] == 'B':
                        # print(self.score_diagonal_up_right[j][0])
                        self._score_diagonal_up_right[j][i]['B'] += 1
                if self._score_diagonal_up_right[j][i]['A'] != 0 and self._score_diagonal_up_right[j][i]['B'] != 0:
                    self._score_diagonal_up_right[j][i]['Score'] = 'X'
                else:
                    self._score_diagonal_up_right[j][i]['Score'] = self._score_diagonal_up_right[j][i]['A'] - self._score_diagonal_up_right[j][i]['B']


    @property
    def score_diagonal_down_right(self):
        return self._score_diagonal_down_right
    
    def __initialise_score_diagonal_down_right(self):
        return [[{
            'A': 0, 
            'B': 0, 
            'Score': 0
            } for x in range(self._rows - 3)] for y in range(self._columns - 3)]

    def _check_diagonals_down_right(self, array):
        for j in range(len(array) - 3):
            for i in range(len(array[j]) - 3):
                for z in range(4):
                    # print('j = ', j, 'i = ', i, 'z = ', z)
                    if array[j + z][i + z] == 'A':
                        self._score_diagonal_down_right[j][i]['A'] += 1
                    elif array[j + z][i + z] == 'B':
                        # print(self.score_diagonal_down_right[j][0])
                        self._score_diagonal_down_right[j][i]['B'] += 1
                if self._score_diagonal_down_right[j][i]['A'] != 0 and self._score_diagonal_down_right[j][i]['B'] != 0:
                    self._score_diagonal_down_right[j][i]['Score'] = 'X'
                else:
                    self._score_diagonal_down_right[j][i]['Score'] = self._score_diagonal_down_right[j][i]['A'] - self._score_diagonal_down_right[j][i]['B']



b1 = Board(7,6)

b1.add_coin(4, 'B')

print(b1.grid)

print(b1.score_row)
print(b1.score_column)
print(b1.score_diagonal_down_right)
print(b1.score_diagonal_up_right)