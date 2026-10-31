class GameStats:
    """记录侧面射击游戏的状态"""

    def __init__(self):
        self.missed_shots = 0 #没有命中目标的子弹数量，初始为 0
        self.game_active = False


    def reset_stats(self):
        """重置每局游戏的统计信息"""
        self.missed_shots = 0