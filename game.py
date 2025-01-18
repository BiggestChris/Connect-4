from tabulate import tabulate
import random
import copy

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
        for i in range(self.rows):
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
        # print('Starting check rows')
        self._score_row = self.__initialise_score_row()
        for j in range(len(array) - 3):
            for i in range(len(array[j])):
                for z in range(4):
                    # print('j = ', j, 'i = ', i, 'z = ', z)
                    if array[j + z][i] == 'A':
                        # print('j = ', j, 'i = ', i, 'z = ', z, 'Array-point before update',self._score_row[j][i]['A'])
                        self._score_row[j][i]['A'] += 1
                        # print('j = ', j, 'i = ', i, 'z = ', z, 'Array-point after update',self._score_row[j][i]['A'])
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
        self._score_column = self.__initialise_score_column()
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
        self._score_diagonal_up_right = self.__initialise_score_diagonal_up_right()
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
        self._score_diagonal_down_right = self.__initialise_score_diagonal_down_right()
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


class ComputerPlayer:
    def __init__(self, difficulty):
        self.difficulty = random

    @property
    def difficulty(self):
        return self._difficulty

    @difficulty.setter
    def difficulty(self, difficulty):
        self._difficulty = difficulty

    def make_move(self, board):
        valid_columns = [col for col in range(len(board.grid)) if board.grid[col][0] == 0]
        # print(valid_columns)
        return random.choice(valid_columns)
        
    #TODO: Determine how to make a move - use Scoring logic of board
    '''
    Pesudo-code:
    1. Read current state of the board
    2. Will any moves give a Win state?
        a. Measure score metrics after each move that could be made
        b. If any Turn+1 score metrics give a Win state, then play in that column
        c. If multiple do, pick one of them at random
    3. Will any moves (or absence of) give a Lost state / Win state to opponent?
        a. Measure score metrics as if current opponent could make a move
        b. If any Turn+1-opponent score metrics give them a Win state, then play in that column
        c. If multiple do, pick one of them at random (no-win situation)
    4. What move will maximise score?
        a. Measure score metrics after each move that could be made
        b. Which move will maximise own score/minimise opponent score? (Offensive vs Defensive?)
            i. Check that the move will not create a potential Win state for the opponent
        c. If multiple with same sccore, pick one of them at random


    How to measure potential board state?
        Create a copy of the board to experiment with, and read score off of that
    '''

    
    def check_for_win(self, board):
        column_wins = []
        directions = ['row', 'column', 'diagonal_up_right', 'diagonal_down_right']
        
        for column_index in range(len(board.grid)):
            dummy_board = copy.deepcopy(board)
            dummy_board.add_coin((column_index + 1), 'B')
            for direction in directions:
                score_attribute = getattr(dummy_board, f'score_{direction}')
                # print(score_attribute)
                for column_cell in score_attribute:
                    for row_cell in column_cell:
                        if row_cell['B'] == 4:
                            column_wins.append(column_index)
                            break  # Breaks out of the innermost loop (row_cell)
                    else:
                        continue  # Continues to the next column_cell
                    break  # Breaks out of the column_cell loop
                else:
                    continue  # Continues to the next direction in total_score
                break  # Breaks out of the direction loop
        print(column_wins)



    def check_for_lose(self, board):
        column_loses = []
        directions = ['row', 'column', 'diagonal_up_right', 'diagonal_down_right']
        
        for column_index in range(len(board.grid)):
            dummy_board = copy.deepcopy(board)
            dummy_board.add_coin((column_index + 1), 'A')
            for direction in directions:
                score_attribute = getattr(dummy_board, f'score_{direction}')
                # print(score_attribute)
                for column_cell in score_attribute:
                    for row_cell in column_cell:
                        if row_cell['A'] == 4:
                            column_loses.append(column_index)
                            break  # Breaks out of the innermost loop (row_cell)
                    else:
                        continue  # Continues to the next column_cell
                    break  # Breaks out of the column_cell loop
                else:
                    continue  # Continues to the next direction in total_score
                break  # Breaks out of the direction loop
        print(column_loses)




    def check_move(self, board):
        # dummy_board = copy.deepcopy(board)
        choice_scores = []
        for column_index in range(len(board.grid)):
            total_score = {
                'row': 0,
                'column': 0,
                'diagonal_up_right': 0,
                'diagonal_down_right': 0
            }
            dummy_board = copy.deepcopy(board)
            dummy_board.add_coin((column_index + 1), 'B')
            # print(dummy_board.score_row)
            # print(dummy_board.score_column)
            # print(dummy_board.score_diagonal_up_right)
            # print(dummy_board.score_diagonal_down_right)
            for key in total_score.keys():
                score_attribute = getattr(dummy_board, f'score_{key}')
                # print(score_attribute)
                for column_cell in score_attribute:
                    for row_cell in column_cell:
                        if row_cell['Score'] != 'X':
                            total_score[key] += row_cell['Score']
            print(sum(total_score.values()))
            choice_scores.append(total_score.values())
        print(choice_scores)

        '''
        for j in range(len(dummy_board.score_row)):
            for i in range(len(dummy_board.score_row[j])):
                if dummy_board.score_row[j][i]['Score'] == 'X':
                    pass
                else:
                    total_score['row'] += dummy_board.score_row[j][i]['Score']
        for j in range(len(dummy_board.score_column)):
            for i in range(len(dummy_board.score_column[j])):
                if dummy_board.score_column[j][i]['Score'] == 'X':
                    pass
                else:
                    total_score['column'] += dummy_board.score_column[j][i]['Score']
        for j in range(len(dummy_board.score_diagonal_up_right)):
            for i in range(len(dummy_board.score_diagonal_up_right[j])):
                if dummy_board.score_diagonal_up_right[j][i]['Score'] == 'X':
                    pass
                else:
                    total_score['diagonal_up_right'] += dummy_board.score_diagonal_up_right[j][i]['Score']
        for j in range(len(dummy_board.score_diagonal_down_right)):
            for i in range(len(dummy_board.score_diagonal_down_right[j])):
                if dummy_board.score_diagonal_down_right[j][i]['Score'] == 'X':
                    pass
                else:
                    total_score['diagonal_down_right'] += dummy_board.score_diagonal_down_right[j][i]['Score']
        print(total_score['row'] + total_score['column'] + total_score['diagonal_up_right'] + total_score['diagonal_down_right'])
        '''
        

    #TODO: Add in further decision logic - fool's mate workaround


class Game:
    #TODO: Initialise the game state (board and player/s)
    def __init__(self):
        self.board = Board(7,6)
        self.computer = ComputerPlayer('random')
        self.win = False
        self.play()

    #TODO: Set rules for how to play - i.e. take it in turns between player and computer
    def play(self):
        while self.win == False:
            player_move = int(input('Input your move as a column, 1-7: '))
            self.board.add_coin(player_move, 'A')
            print(self.board)
            self.check_win()
            if self.win == True: # Feels like there should be a cleaner way to write this
                continue
            print('Computer moving')
            computer_move = self.computer.make_move(self.board)
            self.board.add_coin(computer_move, 'B')
            print(self.board)
            self.check_win()
        else:
            print('Game over')

    #TODO: Identify when the game has been won and declare accordingly (and stop the game)
    def check_win(self):
        directions = ['row', 'column', 'diagonal_up_right', 'diagonal_down_right']

        for direction in directions:
            score_attribute = getattr(self.board, f'score_{direction}')
            for column_cell in score_attribute:
                for row_cell in column_cell:
                    if row_cell['Score'] == 4:
                        self.win = True
                        break


        '''
        for j in range(len(self.board.score_row)):
            for i in range(len(self.board.score_row[j])):
                if self.board.score_row[j][i]['Score'] == 4:
                    self.win = True
                    break
        for j in range(len(self.board.score_column)):
            for i in range(len(self.board.score_column[j])):
                if self.board.score_column[j][i]['Score'] == 4:
                    self.win = True
                    break
        for j in range(len(self.board.score_diagonal_up_right)):
            for i in range(len(self.board.score_diagonal_up_right[j])):
                if self.board.score_diagonal_up_right[j][i]['Score'] == 4:
                    self.win = True
                    break
        for j in range(len(self.board.score_diagonal_down_right)):
            for i in range(len(self.board.score_diagonal_down_right[j])):
                if self.board.score_diagonal_down_right[j][i]['Score'] == 4:
                    self.win = True
                    break
        '''


# game = Game()

board = Board(7, 6)
computer = ComputerPlayer('random')
board.add_coin(3, 'B')
board.add_coin(3, 'B')
board.add_coin(3, 'B')
board.add_coin(2, 'B')
board.add_coin(2, 'B')
board.add_coin(4, 'B')
board.add_coin(4, 'B')
board.add_coin(4, 'B')
board.add_coin(6, 'A')
board.add_coin(6, 'A')
board.add_coin(6, 'A')
print(board)
computer.check_for_win(board)
computer.check_for_lose(board)