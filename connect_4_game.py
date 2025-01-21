import pygame
import sys

class Game_Instance:
    def __init__(self):
        # Game settings
        self.ROWS = 6 # TODO: Link to row variable
        self.COLUMNS = 7 # TODO: Link to column variable
        self.GRID_SIZE = 100 # Should be static, width/height of each cell in the grid
        self.WIDTH = self.COLS * self.GRID_SIZE = # Setting width to be used for screen
        self.HEIGHT = (self.ROWS + 1) * self.GRID_SIZE = # Setting height to be used for screen, want black row at top
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
        self.board = [[0 for _ in range(self.COLS)] for _ in range(self.ROWS)]
        self.running = True
        self.current_player = 1 # Player 1 starts


    def draw_board(self):
        """Draws the Connect 4 board."""
        for row in range(self.ROWS): # TODO: Change to match logic of game board rendering - rows in columns not columns in rows
            for col in range(self.COLS):
                pygame.draw.rect(
                    self.screen, 
                    self.BLUE, 
                    (col * self.GRID_SIZE, row * self.GRID_SIZE + self.GRID_SIZE, self.GRID_SIZE, self.GRID_SIZE)
                )
                color = self.BLACK
                if self.board[row][col] == 1:
                    color = self.RED
                elif board[row][col] == 2:
                    color = self.YELLOW
                pygame.draw.circle(
                    self.screen, 
                    color, 
                    (col * self.GRID_SIZE + self.GRID_SIZE // 2, row * self.GRID_SIZE + self.GRID_SIZE + self.GRID_SIZE // 2), 
                    self.RADIUS,
                )



# Game variables
turn = 1  # 1 = Player 1 (Red), 2 = Player 2 (Yellow)


def draw_board(board):
    """Draws the Connect 4 board."""
    for row in range(ROWS):
        for col in range(COLS):
            pygame.draw.rect(screen, BLUE, (col * GRID_SIZE, row * GRID_SIZE + GRID_SIZE, GRID_SIZE, GRID_SIZE))
            color = BLACK
            if board[row][col] == 1:
                color = RED
            elif board[row][col] == 2:
                color = YELLOW
            pygame.draw.circle(
                screen, color, (col * GRID_SIZE + GRID_SIZE // 2, row * GRID_SIZE + GRID_SIZE + GRID_SIZE // 2), RADIUS
            )


def is_valid_column(board, col):
    """Checks if a column has at least one empty space."""
    return board[0][col] == 0


def get_next_open_row(board, col):
    """Finds the lowest available row in a column."""
    for row in range(ROWS - 1, -1, -1):
        if board[row][col] == 0:
            return row
    return None


def animate_chip_fall(col, target_row, player):
    """Animates the chip falling down to the target row."""
    x = col * GRID_SIZE + GRID_SIZE // 2
    y = GRID_SIZE // 2
    while y < target_row * GRID_SIZE + GRID_SIZE // 2:
        screen.fill(BLACK)  # Clear the screen
        draw_board(board)  # Redraw the current board

        # Draw the falling chip
        pygame.draw.circle(screen, RED if player == 1 else YELLOW, (x, y), RADIUS)

        pygame.display.update()
        pygame.time.delay(20)  # Control animation speed
        y += 10


# Main loop

while running:
    screen.fill(BLACK)
    draw_board(board)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Get the column clicked
            x_pos = event.pos[0]
            col = x_pos // GRID_SIZE

            if is_valid_column(board, col):
                # Determine the next available row
                row = get_next_open_row(board, col)

                # Animate the chip falling
                animate_chip_fall(col, row, turn)

                # Place the chip in the board
                board[row][col] = turn

                # Switch turns
                turn = 3 - turn  # Alternate between 1 and 2

# Clean up and exit
pygame.quit() # Releases resources that Pygame has acquired, such as the display, audio, and input devices
sys.exit() # Terminates the program and closes any running processes.
