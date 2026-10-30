import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """表示单个外星人的类"""

    def __init__(self,ai_settings,screen):
        """初始化外星人"""

        super().__init__() #完成父类的初始化准备
        self.ai_settings = ai_settings
        self.screen = screen #保存绘制用的屏幕

        self.image = pygame.image.load("images/alien.bmp") #加载外星人图片
        self.rect = self.image.get_rect() #获取图片对应的矩形，用来管理位置和大小

        #每个外星人最终都在屏幕左上角附近
        self.rect.x = self.rect.width #self.rect.x：外星人左边缘的 x 坐标
        self.rect.y = self.rect.height #self.rect.y：外星人顶边的 y 坐标

        self.x = float(self.rect.x)


    def check_edges(self):
        """外星人到达屏幕边缘时返回Ture"""
        screen_rect = self.screen.get_rect()

        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """根据编队方向左右移动"""
        self.x += self.ai_settings.alien_speed_factor*self.ai_settings.fleet_direction
        self.rect.x = self.x


#    def blitme(self):
#        """在指定位置绘制外星人"""
#        self.screen.blit(self.image,self.rect) #self.screen：画到哪个屏幕上。