from tabulate import tabulate
import random
import copy
import pygame
import sys

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
        self.difficulty = difficulty

    @property
    def difficulty(self):
        return self._difficulty

    @difficulty.setter
    def difficulty(self, difficulty):
        self._difficulty = difficulty

    def make_move(self, board):
        valid_columns = [col for col in range(len(board.grid)) if board.grid[col][0] == 0]
        print(f'Valid columns are: ', valid_columns)
        match self.difficulty:
            case 'random':
                return random.choice(valid_columns)
            case 'normal':
                # wins = self.check_for_win(board)
                wins = [col for col in self.check_for_win(board) if col in valid_columns]
                if wins:
                    # print('Pick win')
                    return random.choice(wins)
                # loses = self.check_for_lose(board)
                loses = [col for col in self.check_for_lose(board) if col in valid_columns]
                if loses:
                    # print('Pick avoid lose')
                    return random.choice(loses)
                # fools = self.check_for_fool(board)
                fools = [col for col in self.check_for_fool(board) if col in valid_columns]
                if fools:
                    return random.choice(fools)
                moves = self.check_move(board)

                for move in moves:
                    if move in valid_columns:
                        return move

                print('No more valid moves')
                return 'X'

        
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
        # print(column_wins)
        return column_wins



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
        # print(column_loses)
        return column_loses

    def check_for_fool(self, board):
        moves = []
        for z in range(len(board.grid)):
            try:
                if (board.grid[z][-1] == 'A'
                and board.grid[z + 1][-1] == 'A'
                and (
                    (
                        (board.grid[z - 1][-1] == 0 
                        and board.grid[z - 2][-1] == 0
                        and board.grid[z + 2][-1] == 0
                        )
                    )
                    or
                    (
                        (board.grid[z - 1][-1] == 0 
                        and board.grid[z + 2][-1] == 0
                        and board.grid[z + 3][-1] == 0
                        )
                    )
                )):
                    moves.append(z - 1)
                    moves.append(z + 2)
                elif (board.grid[z][-1] == 'A'
                and board.grid[z + 2][-1] == 'A'
                and (
                    board.grid[z - 1][-1] == 0
                    and board.grid[z + 1][-1] == 0
                    and board.grid[z + 3][-1] == 0
                )):
                    moves.append(z + 1)
            except IndexError:
                continue
        return moves


    def check_move(self, board):
        # TODO: Don't let computer make invalid move
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
            print('Column is: ', column_index, 'Score is: ', sum(total_score.values()))
            # If move causes a lose add a very high number
            losses = self.check_for_lose(dummy_board)
            if losses:
                choice_scores.append(sum(total_score.values()) + 1000)
            else: 
                choice_scores.append(sum(total_score.values()))
        # print(choice_scores)

        # check this move won't cause a lose
        # new_dummy_board = copy.deepycopy(dummy_board.add_coin((choice_scores.index(min(choice_scores)) + 1), 'B'))
        # self.check_for_lose(new_dummy_board)
        print(f'Choice scores is: ', choice_scores)
        # Get indices sorted by score from min to max
        sorted_indices = [index for index, _ in sorted(enumerate(choice_scores), key=lambda x: x[1])]
        
        return sorted_indices

        # return choice_scores.index(min(choice_scores))




class Game:
    def __init__(self):
        self.board = Board(7,6)
        self.computer = ComputerPlayer('normal')
        self.win = False
        self.winner = False
        # self.play()

    '''
    Below is a method to play the game in terminal leaving it in in case it may ever be needed for debugging, but
    leaving it in as could be useful for trouble-shooting in the future
    '''
    def play(self):
        if random.choice([1,2]) == 2:
            print('Computer starts')
            computer_move = self.computer.make_move(self.board)
            self.board.add_coin(computer_move + 1, 'B')
            print(self.board)
            self.check_win()
        else:
            print('Player starts')
        while self.win == False:
            player_move = int(input('Input your move as a column, 1-7: '))
            self.board.add_coin(player_move, 'A')
            print(self.board)
            self.check_win()
            if self.win == True: # Feels like there should be a cleaner way to write this
                continue
            print('Computer moving')
            computer_move = self.computer.make_move(self.board)
            self.board.add_coin(computer_move + 1, 'B')
            print(self.board)
            self.check_win()
        else:
            if self.winner == 4:
                print('You win')
            elif self.winner == -4:
                print('You lose')
            else:
                print('Whoops, something has gone wrong! Game over though')

    def check_win(self):
        directions = ['row', 'column', 'diagonal_up_right', 'diagonal_down_right']

        for direction in directions:
            score_attribute = getattr(self.board, f'score_{direction}')
            for column_cell in score_attribute:
                for row_cell in column_cell:
                    if row_cell['Score'] == 4 or row_cell['Score'] == -4:
                        self.win = True
                        self.winner = row_cell['Score']
                        break



'''
game = Game()
board = Board(7, 6)
computer = ComputerPlayer('random')
print(board)
computer.check_for_win(board)
computer.check_for_lose(board)
'''

class Visual_Game_Instance:
    def __init__(self):
        # Create game state
        self.game = Game()
        # Game settings
        self.ROWS = self.game.board.rows # Can load in as static as these won't/shouldn't change
        self.COLS = self.game.board.columns # Can load in as static as these won't/shouldn't change

        # Game visuals
        self.GRID_SIZE = 100 # Should be static, width/height of each cell in the grid
        self.WIDTH = self.COLS * self.GRID_SIZE # Setting width to be used for screen
        self.HEIGHT = (self.ROWS + 1) * self.GRID_SIZE # Setting height to be used for screen, want black row at top
        self.RADIUS = self.GRID_SIZE // 2 - 5 # Setting radius of chips, want it to be half grid-width, then just a tad smaller than that
        self.BLUE = (0, 0, 255) # Defining blue colour
        self.BLACK = (0, 0, 0) # Defining black colour
        self.RED = (255, 0, 0) # Defining red colour
        self.YELLOW = (255, 255, 0) # Defining yellow colour

        # Initialize Pygame
        pygame.init()
        # Create the screen
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Connect 4")

        # Game state
        # self.board = [[0 for _ in range(self.COLS)] for _ in range(self.ROWS)] # TODO: Ensure this only relates to rendering
        self.state = "menu"  # Start in the menu state
        self.running = True
        self.current_player = 'A' # Player 1 starts #TODO: Have this dictated by game logic


    def draw_board(self):
        """Draws the Connect 4 board."""
        for col in range(self.COLS): # TODO: Change to match logic of game board rendering - rows in columns not columns in rows
            for row in range(self.ROWS):
                pygame.draw.rect(
                    self.screen, 
                    self.BLUE, 
                    (col * self.GRID_SIZE, row * self.GRID_SIZE + self.GRID_SIZE, self.GRID_SIZE, self.GRID_SIZE)
                )
                color = self.BLACK
                if self.game.board.grid[col][row] == 'A':
                    color = self.RED
                elif self.game.board.grid[col][row] == 'B':
                    color = self.YELLOW
                pygame.draw.circle(
                    self.screen, 
                    color, 
                    (col * self.GRID_SIZE + self.GRID_SIZE // 2, row * self.GRID_SIZE + self.GRID_SIZE + self.GRID_SIZE // 2), 
                    self.RADIUS,
                )


    def handle_events(self):
        """Handle user input and game events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and self.current_player == 'A':
                col = event.pos[0] // self.GRID_SIZE
                if self.is_valid_location(col) and self.game.win == False:
                    # self.game.board.add_coin(col + 1, self.current_player)
                    row = self.get_next_open_row(col)
                    print(f"Player target_row: {row}")
                    # Animate the chip falling
                    self.animate_chip_fall(col, row, self.current_player)
                    self.game.board.add_coin(col + 1, self.current_player)
                    # self.board[row][col] = self.current_player
                    '''
                    if self.check_win(self.current_player):
                        print(f"Player {self.current_player} wins!")
                        self.running = False
                    '''
                    # Check for win or switch turns
                    self.game.check_win()
                    if self.game.win:
                        break
                        # self.running = False
                    else:
                        self.current_player = 'B'  # Switch to computer
                        self.computer_turn()

    def computer_turn(self):
        # Handle the computer's move.
        print("Computer's turn...")
        computer_move = self.game.computer.make_move(self.game.board)
        if computer_move is not None:
            if computer_move == 'X':
                print('Game draw')
            else:
                row = self.get_next_open_row(computer_move)
                print(f"Computer target_row: {row}")
                self.animate_chip_fall(computer_move, row, 'B')
                self.game.board.add_coin(computer_move + 1, 'B')

                # Check for win or switch back to player
                self.game.check_win()
                if self.game.win:
                    print(f"Player {self.current_player} wins!")
                    # self.running = False
                else:
                    self.current_player = 'A'  # Switch back to player


    
    def is_valid_location(self, col):
        """Check if the column is a valid move."""
        return self.game.board.grid[col][0] == 0
    

    def get_next_open_row(self, col):
        """Get the next open row in the column."""
        for row in range(self.ROWS -1, -1, -1):
            if self.game.board.grid[col][row] == 0:
                return row
            

    def animate_chip_fall(self, col, target_row, player):
        """Animates the chip falling down to the target row."""
        x = col * self.GRID_SIZE + self.GRID_SIZE // 2
        y = self.GRID_SIZE // 2
        while y < (target_row * self.GRID_SIZE + self.GRID_SIZE // 2):
            self.screen.fill(self.BLACK)  # Clear the screen
            self.draw_board()  # Redraw the current board

            # Draw the falling chip
            pygame.draw.circle(self.screen, self.RED if player == 'A' else self.YELLOW, (x, y), self.RADIUS)

            pygame.display.update()
            pygame.time.delay(20)  # Control animation speed
            y += 10
            
    '''
    def check_win(self, player):
        #TODO: Refactor this, as want to use game logic to determine win
        """Check if the current player has won."""
        # Horizontal check
        for row in range(self.ROWS):
            for col in range(self.COLS - 3):
                if all(self.board[row][col + i] == player for i in range(4)):
                    return True
        # Vertical check
        for col in range(self.COLS):
            for row in range(self.ROWS - 3):
                if all(self.board[row + i][col] == player for i in range(4)):
                    return True
        # Positive diagonal
        for row in range(self.ROWS - 3):
            for col in range(self.COLS - 3):
                if all(self.board[row + i][col + i] == player for i in range(4)):
                    return True
        # Negative diagonal
        for row in range(3, self.ROWS):
            for col in range(self.COLS - 3):
                if all(self.board[row - i][col + i] == player for i in range(4)):
                    return True
        return False
    '''
        

    def run(self):
        """Main game loop."""
        while self.running:
            if self.state == "menu":
                self.main_menu()
            elif self.state == "play":
                self.play_game()
            elif self.state == "exit":
                self.running = False
            
            pygame.display.update()

        pygame.quit()
        sys.exit()


    def main_menu(self):
        """Main Menu logic."""
        font = pygame.font.Font(None, 48)
        menu_text = font.render("Main Menu - Press P to Play or Q to Quit", True, (255, 255, 255))
        text_rect = menu_text.get_rect(center=(self.WIDTH // 2, self.HEIGHT // 2))
        
        self.screen.fill((0, 0, 0))
        self.screen.blit(menu_text, text_rect)
        pygame.display.flip()

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.state = "exit"
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    self.state = "play"
                elif event.key == pygame.K_q:
                    self.state = "exit"


    def play_game(self):
        self.screen.fill(self.BLACK)
        self.handle_events()
        self.draw_board() # Always draw the board

        if self.game.win:
            # Render the winning text
            font = pygame.font.Font(None, 48)
            text_surface = font.render(f"Player {'A' if self.game.winner == 4 else 'B'} wins!", True, (255, 255, 255))
            text_rect = text_surface.get_rect(center=(self.WIDTH // 2, self.GRID_SIZE // 2))
            self.screen.blit(text_surface, text_rect)
        
        pygame.display.update()


if __name__ == "__main__":
    game = Visual_Game_Instance()
    game.run()


'''
    What is still neededed?
    1. A start menu, want to be able to pick 1-player or 2-player. Want to pick computer difficulty.
    2. Clear win or lose relay in the game, then bring people back to main menu.
    3. Multiple computer difficulties (Easy/Medium/Hard seems sensible).
    4. Set up for Pygbag
'''