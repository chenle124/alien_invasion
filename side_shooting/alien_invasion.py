import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_functions as gf
from target import Target
from game_stats import GameStats

def run_game():
    pygame.init() #初始化Pygame，为使用它的功能做好准备

    ai_settings = Settings()

    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height)) #pygame.display：Pygame 中负责窗口显示的模块。set_mode()：创建游戏的显示窗口
    pygame.display.set_caption("Alien Invasion") #设置窗口顶部标题栏的文字

    ship = Ship(ai_settings,screen)
    bullets = Group() #编组 Group 可以理解为专门管理精灵对象的容器。

    target = Target(screen)

    stats = GameStats()

    while True:
        gf.check_events(ai_settings, screen, ship, bullets)

        if stats.game_active:
            ship.update() #更新一艘飞船的位置
            target.update()
            gf.update_bullets(bullets,stats)

            if stats.game_active: #碰撞检测使用的是本轮更新后的位置。第二个 if 则确保第三次未命中后，本轮不再处理目标碰撞。
                gf.check_bullet_target_collision(bullets,target)

        gf.update_screen(ai_settings,screen,ship,bullets,target)

run_game()