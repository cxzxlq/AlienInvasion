import sys

import pygame

class AlienInvasion:
    
    def __init__(self):
        """初始化游戏并创建游戏资源"""
        pygame.init()

        self.screen = pygame.display.set_mode((1500, 750))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """开始游戏主循环"""
        while True:
            #监视键盘和鼠标事件
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            #让最近绘制屏幕可见0
            pygame.display.flip()

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()