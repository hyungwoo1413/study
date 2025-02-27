import pygame
from pygame.locals import *
from pygame.draw import *
import sys


class omok():

    def __init__(self):
        pygame.init()
        self.Surface = pygame.display.set_mode((800, 800))
        self.FPSCLOCK = pygame.time.Clock()
        pygame.display.set_caption('omok')
        self.turn = False
        self.isPlaying = True
        self.board = [[None for _ in range(19)] for _ in range(19)]
        
    def main(self):
        while True:
            self.FPSCLOCK.tick(30)
            self.Surface.fill('#DCB35C')

            # 게임판 그리기
            for x in range(40, (40 * 19) + 1, 40):
                line(self.Surface, 'black', (x, 40), (x, 40 * 19))
            for y in range(40, (40 * 19) + 1, 40):
                line(self.Surface, 'black', (40, y), (40 * 19, y))
                
            pygame.display.update()
            self.event()
            

    def event(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONUP: # 마우스 클릭
                    if event.button == 1:
                        if not self.isPlaying:
                            continue
                        else:
                            self.find_xy(pygame.mouse.get_pos()) 
                            pygame.display.update()


    def find_xy(self, xy):
        x = xy[0]
        y = xy[1]

        # 클릭된 위치를 grid에 맞추기
        for i in range(0, 720 + 1, 40):
            if 20 + i <= x <= 60 + i:
                x_dot = i + 40
            if 20 + i <= y <= 60 + i:
                y_dot = i + 40

        x_idx = (x_dot // 40) - 1
        y_idx = (y_dot // 40) - 1
        
        if self.board[x_idx][y_idx] is None:
            if self.turn == False: 
                circle(self.Surface, (0, 0, 0), (x_dot, y_dot), 19) # 검은색 돌
                self.board[x_idx][y_idx] = (x_dot, y_dot, 'white')
                if self.check_win(x_idx, y_idx, 'white'):  # 승리 체크
                    self.win()
                self.turn = True
            else: 
                circle(self.Surface, (255, 255, 255), (x_dot, y_dot), 19) # 흰색 돌
                self.board[x_idx][y_idx] = (x_dot, y_dot, 'black')
                if self.check_win(x_idx, y_idx, 'black'):  # 승리 체크
                    self.win()
                self.turn = False
        else:
            return

    # ===================================================================================================================================

    def check_win(self, x_idx, y_idx, color):
        # (x_idx, y_idx) 위치에 놓은 색의 돌에 대해 승리 조건 체크
        directions = [
            (1, 0),  # 가로 방향 (x 증가)
            (0, 1),  # 세로 방향 (y 증가)
            (1, 1),  # 오른쪽 대각선 (x, y 둘 다 증가)
            (1, -1)  # 왼쪽 대각선 (x 증가, y 감소)
        ]
        
        for dx, dy in directions:
            count = 1  # 놓은 돌을 포함해서 시작
            # 왼쪽/위 방향 탐색
            i = 1
            while 0 <= x_idx + dx * i < 19 and 0 <= y_idx + dy * i < 19:
                if self.board[x_idx + dx * i][y_idx + dy * i] and self.board[x_idx + dx * i][y_idx + dy * i][2] == color:
                    count += 1
                else:
                    break
                i += 1
            # 오른쪽/아래 방향 탐색
            i = 1
            while 0 <= x_idx - dx * i < 19 and 0 <= y_idx - dy * i < 19:
                if self.board[x_idx - dx * i][y_idx - dy * i] and self.board[x_idx - dx * i][y_idx - dy * i][2] == color:
                    count += 1
                else:
                    break
                i += 1

            if count >= 5:  # 연속된 5개의 돌이 있으면 승리
                return True

        return False
    
    # ===================================================================================================================================

    def win(self):
        myfont = pygame.font.SysFont('NanumGothic', 50)
        black_win = myfont.render('BLACK WIN', True, 'black')
        white_win = myfont.render('WHITE WIN', True, 'white')

        self.isPlaying = False # 게임종료

        if self.turn:
            self.Surface.blit(white_win, (300, 5))
        else:
            self.Surface.blit(black_win, (300, 5))


if __name__ == '__main__':
    game = omok()
    game.main()
