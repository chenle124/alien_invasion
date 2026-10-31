import pygame.font

class Button:
    """表示游戏中的按钮"""

    def __init__(self,screen,msg):
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

        self.prep_msg(msg)


    def prep_msg(self,msg):
        """将文字转换为图像，并让它在按钮中央显示"""

        self.msg_image = self.font.render(msg,True,self.text_color,self.button_color) #把 msg 中的文字转换成图像。`True` 表示让文字边缘更平滑，后两个参数分别指定文字颜色和背景颜色。
        self.msg_image_rect = self.msg_image.get_rect() #获取文字图像的矩形
        self.msg_image_rect.center = self.rect.center #两个矩形的 center 相同：让文字位于按钮中央