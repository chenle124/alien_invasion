import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_functions as gf
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

def run_game():
    pygame.init() #初始化Pygame，为使用它的功能做好准备

    ai_settings = Settings()

    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height)) #pygame.display：Pygame 中负责窗口显示的模块。set_mode()：创建游戏的显示窗口
    pygame.display.set_caption("Alien Invasion") #设置窗口顶部标题栏的文字

    ship = Ship(ai_settings,screen)
    bullets = Group() #编组 Group 可以理解为专门管理精灵对象的容器。
    aliens = Group() #管理多个外星人的编组

    gf.create_fleet(ai_settings,screen,aliens,ship)

    stats = GameStats(ai_settings) #创建记录游戏统计信息的对象

    play_button = Button(screen,"Play")

    sb = Scoreboard(ai_settings,screen,stats) #必须先创建 stats，才能把它传给 Scoreboard

    while True:
        gf.check_events(ai_settings,screen,aliens,ship,bullets,stats,play_button)

        if stats.game_active: #游戏结束后，窗口会保留，画面中的物体停止移动。
            ship.update() #更新一艘飞船的位置
            gf.update_bullets(ai_settings,screen,aliens,ship,bullets)
            gf.update_aliens(ai_settings,screen,ship,aliens,bullets,stats)

        gf.update_screen(ai_settings,screen,ship,aliens,bullets,stats,play_button,sb)

run_game()