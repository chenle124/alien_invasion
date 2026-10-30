class Settings:
    """存储游戏的所有设置"""

    def __init__(self):
        """初始化游戏的设置"""

        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)

        self.ship_speed_factor = 1.5 #表示飞船每轮循环移动的距离

        #子弹设置
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 3 #表示最多同时保留 3 颗子弹，不是整局只能发射 3 颗。