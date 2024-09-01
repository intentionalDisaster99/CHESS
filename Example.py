import pygame as pg

# Initialize Pygame
pg.init()

# Set up the display
WIDTH, HEIGHT = 700, 700  # Size of the chessboard window
SQUARE_SIZE = WIDTH // 8  # Each square is one-eighth of the board
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("CHESS")

# Define colors
WHITE = (236, 207, 174)
BLACK = (198, 100, 57)

# Function to draw the chessboard
def draw_chessboard():
    for row in range(8):
        for col in range(8):
            # Determine the color of the square
            color = WHITE if (row + col) % 2 == 0 else BLACK
            # Draw the square
            pg.draw.rect(screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))



# Main loop
if __name__ == "__main__":
    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        # Draw the chessboard
        draw_chessboard()

        # Update the display
        pg.display.flip()

# Quit Pygame
pg.quit()
