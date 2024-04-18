import pygame

ROWS = 6
COLS = 7
CIRCLE_RADIUS = 50
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
EMPTY = (255, 255, 255)
LINE_COLOR = (0, 0, 0)
WINNING_LENGTH = 4

pygame.init()
screen = pygame.display.set_mode((700, 600))
pygame.display.set_caption("Крестики-нолики")
clock = pygame.time.Clock()
running = True

# создание матрицы пустых клетов
board =[]
for _ in range(ROWS):
    row = []
    for _ in range(COLS):
        row.append(EMPTY)
    board.append(row)

def draw_board():
    for row in range(ROWS):
        for col in range(COLS):
            pygame.draw.circle(screen, board[row][col],
                               (col * 2 * CIRCLE_RADIUS + CIRCLE_RADIUS,
                                row * 2 * CIRCLE_RADIUS + CIRCLE_RADIUS),
                                CIRCLE_RADIUS)
    pygame.display.flip()


def check_winner():

    for row in range(ROWS):
        for col in range(COLS - 3):
            if board[row][col] == board[row][col + 1] == board[row][col + 2] == board[row][col + 3] != EMPTY:
                return board[row][col]


    for col in range(COLS):
        for row in range(ROWS - 3):
            if board[row][col] == board[row + 1][col] == board[row + 2][col] == board[row + 3][col] != EMPTY:
                return board[row][col]


current_player = RED
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            col = x // (2 * CIRCLE_RADIUS)

            for row in range(ROWS):
                if board[row][col] == EMPTY:
                    board[row][col] = current_player
                    winner = check_winner()
                    if winner:
                        print("Победитель:", "Красный" if winner == RED else "Желтый")
                        running = False
                    else:
                        current_player = YELLOW if current_player == RED else RED
                    break


    screen.fill((100, 149, 237))

    draw_board()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
