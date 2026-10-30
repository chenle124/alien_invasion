import pygame

class Target:
    """表示屏幕右侧的射击目标"""

    def __init__(self,screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.color = (60,60,60)
        self.rect = pygame.Rect(0,0,30,100) #创建宽 30、高 100 的矩形

        #放在屏幕右侧，垂直居中
        self.rect.right = self.screen_rect.right - 30
        self.rect.centery = self.screen_rect.centery

        self.y = float(self.rect.y)
        self.speed = 0.5 
        self.direction = 1 #`direction` 为 1 表示向下，为 -1 表示向上


    def update(self):
        """上下移动目标，碰到边缘后反向"""
        self.y += self.speed * self.direction
        self.rect.y = self.y

        if self.rect.bottom >= self.screen_rect.bottom:
            self.rect.bottom = self.screen_rect.bottom
            self.y = float(self.rect.y)
            self.direction = -1

        elif self.rect.top <= self.screen_rect.top:
            self.rect.top = self.screen_rect.top
            self.y = float(self.rect.y)
            self.direction = 1

    def draw_target(self):
        """绘制目标"""

        pygame.draw.rect(self.screen,self.color,self.rect)