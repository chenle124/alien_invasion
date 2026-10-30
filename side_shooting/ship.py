from pathlib import Path

import pygame

class Ship:
    def __init__(self,ai_settings,screen):
        """初始化飞船并设置其起始位置"""

        self.screen = screen #右边的 screen：接收主程序传来的屏幕对象，是方法的参数。
        self.ai_settings = ai_settings #self.ai_settings：是飞船实例的 ai_settings 属性，里面保存的是主程序传进来的设置实例的引用。

        #加载飞船图像并获取其外接矩形
        image_path = Path(__file__).resolve().parent / "images" / "ship.bmp"
        self.image = pygame.image.load(str(image_path)) #pygame.image.load() 读取图片，返回一个表示图片的 Surface 对象
        self.rect = self.image.get_rect() #get_rect() 返回一个 Rect 对象，保存这个框的大小和位置。
        self.screen_rect = screen.get_rect()

        #将每艘新飞船放在屏幕底部中央
        self.rect.left = self.screen_rect.left #飞船左边缘贴着屏幕左边缘
        self.rect.centery = self.screen_rect.centery #飞船在垂直方向居中

        self.center_y = float(self.rect.centery) #self.center是浮点数

        self.moving_down = False
        self.moving_up = False


    def update(self):
        """根据移动标志调整飞船位置"""

        if self.moving_down and self.rect.bottom < self.screen_rect.bottom: #屏幕左边缘的 x 坐标固定为 0，右边缘的 x 坐标则取决于屏幕宽度。
            self.center_y += self.ai_settings.ship_speed_factor
        
        if self.moving_up and self.rect.top >0: #也可以写成：self.rect.left > self.screen_rect.left
            self.center_y -= self.ai_settings.ship_speed_factor

        self.rect.centery = self.center_y #Pygame 的 Rect 对象规定：它的位置和大小都用整数保存。centerx 是 Rect 的一个属性，所以只能保存整数。


    def blitme(self):
        """在指定位置绘制飞船"""        
        self.screen.blit(self.image,self.rect) #在 self.screen 这块屏幕上，把 self.image 飞船图片画到 self.rect 指定的位置。
