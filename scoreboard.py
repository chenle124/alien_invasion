import pygame.font

class Scoreboard:
    """显示得分信息"""

    def __init__(self,ai_settings,screen,stats):
        """初始化显示得分所需属性"""

        self.screen = screen #在游戏窗口上绘制得分
        self.screen_rect = screen.get_rect() #用来确定得分在屏幕上的位置
        self.ai_settings = ai_settings #获取屏幕背景色
        self.stats = stats #获取当前得分 score

        #设置文字颜色和字体
        self.text_color = (30,30,30)
        self.font = pygame.font.Font(None,48)