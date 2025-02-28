import pygame
import socket
import threading
from pygame.locals import *
from pygame.draw import *
import sys

class OmokServer:

    def __init__(self, host='210.119.12.77', port=5000): # 210.119.12.77
        pygame.init()
        self.Surface = pygame.display.set_mode((800, 800))
        self.FPSCLOCK = pygame.time.Clock()
        pygame.display.set_caption('Omok Game Server')

        self.turn = False
        self.isPlaying = True
        self.board = [[None for _ in range(19)] for _ in range(19)]
        
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((host, port))
        self.server_socket.listen(2)
        print(f"Server started on {host}:{port}")
        
        self.players = []

    def handle_client(self, player_socket, player_address):
        print(f"New player connected: {player_address}")
        
        # 게임 로직 처리 (여기서 각 클라이언트와의 상호작용 처리)
        while True:
            data = player_socket.recv(1024)
            if not data:
                break
            
            # 받은 데이터는 클라이언트의 움직임 정보
            x, y, color = data.decode().split(',')
            x, y = int(x), int(y)
            self.update_game(x, y, color)

        player_socket.close()

    def start_game(self):
        while len(self.players) < 2:
            player_socket, player_address = self.server_socket.accept()
            self.players.append(player_socket)
            # 각 클라이언트마다 새로운 스레드를 만들어 게임 처리
            threading.Thread(target=self.handle_client, args=(player_socket, player_address), daemon=True).start()
        print("Both players connected, game starting...")

    def update_game(self, x, y, color):
        if self.board[x][y] is None:
            self.board[x][y] = color
            # 데이터를 다른 플레이어에게 전달
            self.send_data_to_player(1 if color == 'black' else 0, f"{x},{y},{color}")

    def send_data_to_player(self, player_num, data):
        try:
            self.players[player_num].sendall(data.encode())
        except:
            print(f"Error sending data to player {player_num}")
        
    def main(self):
        while True:
            self.FPSCLOCK.tick(30)
            self.Surface.fill('#DCB35C')
            self.myfont = pygame.font.SysFont('D2Coding', 60)

            # 게임판 그리기
            for x in range(40, (40 * 19) + 1, 40):
                line(self.Surface, 'black', (x, 40), (x, 40 * 19))
            for y in range(40, (40 * 19) + 1, 40):
                line(self.Surface, 'black', (40, y), (40 * 19, y))

            pygame.display.update()

    def handle_events(self):
        # 이벤트 처리 (현재 이 코드에서 이 부분은 기본적 이벤트 처리만 포함)
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

if __name__ == '__main__':
    server = OmokServer()
    server.start_game()
    server.main()
