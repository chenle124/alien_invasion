import sys

import pygame

def check_events(ship):
    """响应键盘和鼠标事件"""
    for event in pygame.event.get(): #逐个处理事件。“事件”就是点击鼠标、按下键盘、点击关闭按钮等操作。
        if event.type == pygame.QUIT: #event.type：当前事件的类型。pygame.QUIT：Pygame 中表示“请求关闭窗口”的常量，注意是大写。
            sys.exit() #退出程序

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ship)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)


def check_keydown_events(event,ship):
    """响应按钮"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True

    elif event.key == pygame.K_LEFT:
        ship.moving_left = True

    elif event.key == pygame.K_UP:
        ship.moving_up = True

    elif event.key == pygame.K_DOWN:
        ship.moving_down = True


def check_keyup_events(event,ship):
    """响应松开"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False

    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

    elif event.key == pygame.K_UP:
        ship.moving_up = False
    
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False


def update_screen(ai_settings,screen,ship):
    screen.fill(ai_settings.bg_color) #顺序很重要：先画背景，再画飞船，最后显示画面。 如果先画飞船再填满背景，飞船就会被背景盖住。
    ship.blitme()
    pygame.display.flip() #更新窗口画面
    