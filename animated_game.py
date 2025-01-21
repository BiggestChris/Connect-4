import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 700, 700
GRID_SIZE = 100
RADIUS = GRID_SIZE // 2 - 5
ROWS, COLS = 6, 7

# Colors
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Connect 4")

# Game variables
board = [[0 for _ in range(COLS)] for _ in range(ROWS)]
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
running = True
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

pygame.quit()
sys.exit()
