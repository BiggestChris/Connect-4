import pygame
import sys

class Visual_Game_Instance:
    def __init__(self):
        # Game settings
        self.ROWS = 6 # TODO: Link to row variable
        self.COLS = 7 # TODO: Link to column variable

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
        self.board = [[0 for _ in range(self.COLS)] for _ in range(self.ROWS)] # TODO: Ensure this only relates to rendering
        self.running = True
        self.current_player = 1 # Player 1 starts #TODO: Have this dictated by game logic


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
                elif self.board[row][col] == 2:
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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                col = event.pos[0] // self.GRID_SIZE
                if self.is_valid_location(col):
                    row = self.get_next_open_row(col)
                    # Animate the chip falling
                    self.animate_chip_fall(col, row, self.current_player)
                    self.board[row][col] = self.current_player
                    if self.check_win(self.current_player):
                        print(f"Player {self.current_player} wins!")
                        self.running = False
                    self.current_player = 3 - self.current_player # Switch player

    
    def is_valid_location(self, col):
        """Check if the column is a valid move."""
        return self.board[0][col] == 0
    

    def get_next_open_row(self, col):
        """Get the next open row in the column."""
        for row in range(self.ROWS -1, -1, -1):
            if self.board[row][col] == 0:
                return row
            

    def animate_chip_fall(self, col, target_row, player):
        """Animates the chip falling down to the target row."""
        x = col * self.GRID_SIZE + self.GRID_SIZE // 2
        y = self.GRID_SIZE // 2
        while y < target_row * self.GRID_SIZE + self.GRID_SIZE // 2:
            self.screen.fill(self.BLACK)  # Clear the screen
            self.draw_board()  # Redraw the current board

            # Draw the falling chip
            pygame.draw.circle(self.screen, self.RED if player == 1 else self.YELLOW, (x, y), self.RADIUS)

            pygame.display.update()
            pygame.time.delay(20)  # Control animation speed
            y += 10
            
    
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


    def run(self):
        """Main game loop."""
        while self.running:
            self.screen.fill(self.BLACK)
            self.handle_events()
            self.draw_board()
            pygame.display.update()

        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    game = Visual_Game_Instance()
    game.run()
