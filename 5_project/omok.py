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
        self.board = [[None for _ in range(19)] for _ in range(19)]
        
    def main(self):
        while True:
            self.FPSCLOCK.tick(30)
            self.Surface.fill('#DCB35C')

            for x in range(40, (40*19)+1, 40):
                line(self.Surface, 'black', (x, 40), (x, 40*19)) # 선 긋기
            for y in range(40, (40*19)+1, 40):
                line(self.Surface, 'black', (40, y), (40*19, y))
            
            pygame.display.update()
            self.event()
    
    def event(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pass
                if event.type == pygame.MOUSEBUTTONUP: # 마우스 클릭
                    self.find_xy(pygame.mouse.get_pos()) 
                    pygame.display.update()

    def find_xy(self, xy):
        x = xy[0]
        y = xy[1]

        for i in range(0, 720+1, 40):
            if 20 + i <= x <= 60 + i:
                x_dot = i + 40
            if 20 + i <= y <= 60 + i:
                y_dot = i + 40

        x_idx = (x_dot//40)-1
        y_idx = (y_dot//40)-1
        
        if self.board[x_idx][y_idx] is None:
            if self.turn == False: 
                circle(self.Surface, (255,255,255), (x_dot, y_dot), 19) # 흰색 돌 그리기
                self.board[x_idx][y_idx] = x_dot, y_dot
                self.turn = True
            else: 
                circle(self.Surface, (0,0,0), (x_dot, y_dot), 19) # 검은색 돌 그리기
                self.board[x_idx][y_idx] = x_dot, y_dot
                self.turn = False
        else:
            return


if __name__=='__main__':
    game = omok()
    game.main()