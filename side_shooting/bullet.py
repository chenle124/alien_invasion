import pygame
from pygame.sprite import Sprite 

class Bullet(Sprite): #Sprite 是 Pygame 提供的类，Bullet 继承它，就能获得用于配合精灵编组管理的基础功能。
    """管理飞船发射的子弹"""

    def __init__(self,ai_settings,screen,ship):
        """初始化子弹"""

        super().__init__() #Sprite 的初始化方法允许不传额外参数
        self.screen = screen

        #在(0,0)处创建一个表示子弹的矩形，再设置正确的位置
        self.rect = pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height) #(左上角的x坐标，左上角的y坐标，宽度，高度)
        self.rect.centery = ship.rect.centery
        self.rect.left = ship.rect.right

        #存储用小数表示的子弹位置
        self.x = float(self.rect.x)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor


    def update(self):
        """向上移动子弹"""

        self.x += self.speed_factor #先计算精确位置。
        self.rect.x = self.x


    def draw_bullet(self):
        """在屏幕上绘制子弹"""

        #对于 pygame.draw.rect()，我们没有在定义它，所以不能在自己的调用代码中修改它的形参顺序。
        pygame.draw.rect(self.screen,self.color,self.rect) #(画到哪块屏幕上，使用什么颜色，矩形的位置和大小) 这里没有指定边框宽度，所以画的是实心矩形。
        