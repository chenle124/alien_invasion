import pygame

class Ship:
    def __init__(self,ai_settings,screen):
        """初始化飞船并设置其起始位置"""

        self.screen = screen #右边的 screen：接收主程序传来的屏幕对象，是方法的参数。
        self.ai_settings = ai_settings #self.ai_settings：是飞船实例的 ai_settings 属性，里面保存的是主程序传进来的设置实例的引用。

        #加载飞船图像并获取其外接矩形
        self.image = pygame.image.load("images/ship.bmp") #pygame.image.load() 读取图片，返回一个表示图片的 Surface 对象
        self.rect = self.image.get_rect() #get_rect() 返回一个 Rect 对象，保存这个框的大小和位置。
        self.screen_rect = screen.get_rect()

        #将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx #让飞船水平居中
        self.rect.bottom = self.screen_rect.bottom #让飞船底边与屏幕底边对齐

        self.center = float(self.rect.centerx) #self.center是浮点数

        self.moving_right = False
        self.moving_left = False


    def update(self):
        """根据移动标志调整飞船位置"""

        if self.moving_right and self.rect.right <self.screen_rect.right: #屏幕左边缘的 x 坐标固定为 0，右边缘的 x 坐标则取决于屏幕宽度。
            self.center += self.ai_settings.ship_speed_factor
        
        if self.moving_left and self.rect.left >0: #也可以写成：self.rect.left > self.screen_rect.left
            self.center -= self.ai_settings.ship_speed_factor

        self.rect.centerx = self.center #Pygame 的 Rect 对象规定：它的位置和大小都用整数保存。centerx 是 Rect 的一个属性，所以只能保存整数。


    def blitme(self):
        """在指定位置绘制飞船"""        
        self.screen.blit(self.image,self.rect) #在 self.screen 这块屏幕上，把 self.image 飞船图片画到 self.rect 指定的位置。


    def center_ship(self):
        """让飞船回到屏幕中央的横向位置"""

        self.rect.center = self.screen_rect.centerx