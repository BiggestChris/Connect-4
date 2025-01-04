from tabulate import tabulate

class Board:
    # Initialise the object based on number of columns and rows
    def __init__(self, columns, rows):
        self.columns = columns
        self.rows = rows
        self._grid = self.__initialise_grid()
        
    def __str__(self):
        # Transpose the grid using zip and unpacking
        transposed_grid = list(map(list, zip(*self.grid)))
        return tabulate(transposed_grid, tablefmt="grid", colalign=("center","center"))


    def __initialise_grid(self):
        # Create the grid as an array of dimension equal to number of columns, each of those indices has an array of dimension equal to number of rows
        new_grid = []
        for number in range(1, self._columns + 1):
            col = [number]
            for next_number in range(self._rows):
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
            if self.grid[(number - 1)][(-1 - i)] == 0:
                self._grid[(number - 1)][(-1 - i)] = player
                break
        # print(self.grid[(number - 1)])

        # TODO: Control around adding when full

#TODO: Write in a function for two people to play the game (alternating turns)
#TODO: Write in an algorithm for an computer to play the game a virtual opponent
#TODO: Identify if someone has won the game
#TODO: Identify allowed/unallowed moves

    '''How to identify if someone has won the game
    '''

    score = {'X': 0, 'Y': 0}

    for i in range(self.rows):
        for j in range (self.columns):
            if self.grid[i][j] != 0:
                score[self.grid[i][j]] += 1
                # need to use recursion to dive in

    def check(self, i, j , z, score):
        if (self.grid[i][j] != z) :
            return
        else:
            score[z] += 1
            check(self, i, (j + 1), z, score)
            check(self, (i + 1), (j - 1) , z, score)
            check(self, (i + 1), (j) , z, score)
            check(self, (i + 1), (j + 1) , z, score)
        # Need to track which level of recursion this is
        # Might make sense to put a direction in the check function


b1 = Board(6,5)

print(b1)

b1.add_coin(3, 'Y')
b1.add_coin(3, 'X')
b1.add_coin(3, 'Y')
b1.add_coin(3, 'Y')
b1.add_coin(3, 'Y')

print(b1)