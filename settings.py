class Settings:
    """存储游戏的所有设置"""

    def __init__(self):
        """初始化游戏的设置"""

        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)

        #飞机设置
        self.ship_speed_factor = 3 #表示飞船每轮循环移动的距离
        self.ship_limit = 3 #保存游戏开始时的飞机数量

        #子弹设置
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 3 #表示最多同时保留 3 颗子弹，不是整局只能发射 3 颗。

        #外星人设置
        self.alien_speed_factor = 2

        self.fleet_drop_speed = 10 #每次碰到边缘，整个编队向下移动 10 像素
        self.fleet_direction = 1 #水平移动方向：`1` 向右，`-1` 向左