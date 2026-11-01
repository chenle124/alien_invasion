class GameStats:
    """跟踪游戏的统计信息"""

    def __init__(self,ai_settings):
        """初始化游戏的统计信息"""

        self.ai_settings = ai_settings
        self.reset_stats() #调用当前实例的重置方法。

        #游戏启动时先处于非活跃状态
        self.game_active = False


    def reset_stats(self):
        """重置游戏运行期间会变化的统计信息"""

        self.ships_left = self.ai_settings.ship_limit

        self.score = 0