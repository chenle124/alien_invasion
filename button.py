import pygame.font

class Button:
    """表示游戏中的按钮"""

    def __init__(self,screen):
        """初始化按钮的属性"""

        self.screen = screen
        self.screen_rect = screen.get_rect()

        #按钮大小和颜色
        self.width,self.height = 200,50
        self.button_color = (0,255,0)
        self.text_color = (255,255,255)

        #用于绘制文字的字体
        self.font = pygame.font.SysFont(None,48) #创建一个字体对象，之后用它把文字转换成可以绘制的图像。`None` 表示使用默认字体，`48` 指定字体大小。

        #创建矩形按钮，并放置在屏幕中央
        self.rect = pygame.Rect(0,0,self.width,self.height)
        self.rect.center = self.screen_rect.center