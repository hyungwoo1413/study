import socketio
import pygame
from pygame.locals import *
from pygame.draw import *
import sys

sio = socketio.Client()

# Pygame setup
pygame.init()
Surface = pygame.display.set_mode((800, 800))
FPSCLOCK = pygame.time.Clock()
pygame.display.set_caption('Omok Game')
myfont = pygame.font.SysFont('D2Coding', 60)

# Game state variables
board = [[None for _ in range(19)] for _ in range(19)]
turn = False
isPlaying = True

# SocketIO event handlers
@sio.event
def connect():
    print("연결 완료")

@sio.event
def disconnect():
    print("연결 해제")

@sio.on('update_board')
def on_update_board(data):
    global board
    board = data
    redraw_board()

@sio.on('game_over')
def on_game_over(data):
    winner = data['winner']
    game_over_screen(winner)

# Redrawing the board
def redraw_board():
    Surface.fill('#DCB35C')
    
    for x in range(40, (40 * 19) + 1, 40):
        line(Surface, 'black', (x, 40), (x, 40 * 19))
    for y in range(40, (40 * 19) + 1, 40):
        line(Surface, 'black', (40, y), (40 * 19, y))

    for x in range(19):
        for y in range(19):
            if board[x][y] == 'black':
                circle(Surface, (0, 0, 0), (40 * x + 40, 40 * y + 40), 19)
            elif board[x][y] == 'white':
                circle(Surface, (255, 255, 255), (40 * x + 40, 40 * y + 40), 19)

    pygame.display.update()

# Game over screen
def game_over_screen(winner):
    Surface.fill('#DCB35C')
    winner_text = myfont.render(f'{winner} 승리', True, 'white' if winner == 'black' else 'black')
    Surface.blit(winner_text, (270, 350))
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    reset_game()

# Reset the game
def reset_game():
    global board, turn, isPlaying
    board = [[None for _ in range(19)] for _ in range(19)]
    turn = False
    isPlaying = True
    redraw_board()

# Event handling for mouse clicks
def event_handler():
    global turn, isPlaying
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1 and isPlaying:
                x, y = pygame.mouse.get_pos()
                x_idx = (x - 40) // 40
                y_idx = (y - 40) // 40

                if 0 <= x_idx < 19 and 0 <= y_idx < 19 and board[x_idx][y_idx] is None:
                    color = 'black' if turn else 'white'
                    board[x_idx][y_idx] = color
                    sio.emit('make_move', {'x_idx': x_idx, 'y_idx': y_idx, 'color': color})
                    turn = not turn

if __name__ == "__main__":
    sio.connect('http://localhost:5000')
    while True:
        event_handler()
        FPSCLOCK.tick(30)
