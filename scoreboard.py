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

        self.prep_score()


    def prep_score(self):
        """将得分转换为图像"""

        rounded_score = round(self.stats.score,-1) #round(..., -1) 表示圆整到十位
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str,True,self.text_color,self.ai_settings.bg_color)

        #将得分放到屏幕右上角
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right-20
        self.score_rect.top = 20


    def show_score(self):
        """在屏幕上显示得分"""

        self.screen.blit(self.score_image,self.score_rect)