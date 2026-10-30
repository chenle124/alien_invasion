import pygame

from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    pygame.init() #初始化Pygame，为使用它的功能做好准备
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height)) #pygame.display：Pygame 中负责窗口显示的模块。set_mode()：创建游戏的显示窗口
    pygame.display.set_caption("Alien Invasion")

    ship = Ship(ai_settings,screen)

    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings,screen,ship)

run_game()