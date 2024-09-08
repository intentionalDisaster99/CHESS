import pygame as pg


# CONSTANTS
STARTING_POSITION = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"

PIECES = []
PIECE_LOOKUP = ["b1", "b2", "b3", "b4", "n1", "n2", "n3", "n4", "k1", "k2", "q", "r", "p", "B1", "B2", "B3", "B4", "N1", "N2", "N3", "N4", "K1", "K2", "Q", "R", "P"]

# Set up the display
WIDTH, HEIGHT = 700, 700  # Size of the chessboard window
SQUARE_SIZE = WIDTH // 8  # Each square is one-eighth of the board
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("CHESS")

# Define colors
WHITE = (236, 207, 174)
BLACK = (198, 100, 57)


# Initialize Pygame
pg.init()

# Loading all of the images that we will use
def load_pieces():

    piecesW = []
    piecesB = []
    


    # Getting the pieces out 
    bigBlackPieceImage = pg.image.load('Assets\\Top Down\\Pieces\\Black\\Wood.png').convert()
    bigWhitePieceImage = pg.image.load('Assets\\Top Down\\Pieces\\White\\Wood.png').convert()

    # Making the background to be transparent
    bigBlackPieceImage.set_colorkey((0, 128, 128))
    bigWhitePieceImage.set_colorkey((0, 0, 0))

    # Getting each of the pieces
    for y in range(4):
        for x in range(4):

            # The white piece
            piece = pg.Surface((128, 128))
            piece.blit(bigWhitePieceImage, (0, 0), (128 * x, 128 * y, 128, 128))
            piecesW.append(piece)

            # The black piece
            piece = pg.Surface((128, 128)) 
            piece.blit(bigBlackPieceImage, (0, 0), (128 * x, 128 * y, 128, 128))
            piecesB.append(piece)
    
    # Putting them all in the same array
    piecesB.append(piecesW)
    PIECES = piecesB

    piece_position = (WIDTH / 16 - 128/2, HEIGHT / 16 - 128/2)

    screen.blit(PIECES[11], piece_position)

    pg.display.flip()

    # Putting the pieces into one 

# A function to draw a piece in a certain location
def drawPiece(piece, local):

    # Getting the piece image that we need to draw
    pieceIndex = PIECE_LOOKUP.index(piece)
    piece = PIECE


# Function to draw the chessboard
def draw_chessboard():
    for row in range(8):
        for col in range(8):
            # Determine the color of the square
            color = WHITE if (row + col) % 2 == 0 else BLACK
            # Draw the square
            pg.draw.rect(screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))


# Drawing the starting position
def draw_starting():   

    # Drawing the background of the chessboard to clear the board of anything else
    draw_chessboard()

    # Drawing the chess pieces
    load_pieces()





# Main loop
if __name__ == "__main__":
    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        # Initializing all of the pieces
        draw_starting()

        # Update the display
        pg.display.flip()

# Quit Pygame
pg.quit()
