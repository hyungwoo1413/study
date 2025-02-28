import pygame
import socket
import threading
import sys
from pygame.locals import *
from pygame.draw import *

class OmokClient:

    def __init__(self, host='210.119.12.77', port=5000):  # 210.119.12.77
        pygame.init()
        self.Surface = pygame.display.set_mode((800, 800))
        self.FPSCLOCK = pygame.time.Clock()
        pygame.display.set_caption('Omok Game Client')

        self.turn = False
        self.isPlaying = True
        self.board = [[None for _ in range(19)] for _ in range(19)]
        
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((host, port))
        
        self.mycolor = 'black'
        self.myfont = pygame.font.SysFont('D2Coding', 60)

    def main(self):
        while True:
            self.FPSCLOCK.tick(30)
            self.Surface.fill('#DCB35C')

            # Draw the game board
            for x in range(40, (40 * 19) + 1, 40):
                line(self.Surface, 'black', (x, 40), (x, 40 * 19))
            for y in range(40, (40 * 19) + 1, 40):
                line(self.Surface, 'black', (40, y), (40 * 19, y))
            
            pygame.display.update()
            self.handle_events()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1 and self.isPlaying and self.turn:
                    x, y = pygame.mouse.get_pos()
                    x_idx = (x - 40) // 40
                    y_idx = (y - 40) // 40
                    self.send_move(x_idx, y_idx)

    def send_move(self, x, y):
        move_data = f"{x},{y},{self.mycolor}"
        self.client_socket.sendall(move_data.encode())
        self.turn = False

    def receive_move(self):
        while True:
            move_data = self.client_socket.recv(1024).decode()
            x, y, color = move_data.split(',')
            x, y = int(x), int(y)

            if color == 'black':
                circle(self.Surface, (0, 0, 0), (40 + x * 40, 40 + y * 40), 19)
            else:
                circle(self.Surface, (255, 255, 255), (40 + x * 40, 40 + y * 40), 19)

            self.board[x][y] = color
            self.turn = True

    def start(self):
        # 수신과 송신을 각각 별도의 스레드로 실행
        threading.Thread(target=self.receive_move, daemon=True).start()
        self.main()

if __name__ == '__main__':
    client = OmokClient()
    client.start()
