import sys

import pygame

from bullet import Bullet
from alien import Alien

def check_events(ai_settings, screen, ship, bullets):
    """响应键盘和鼠标事件"""

    for event in pygame.event.get(): #逐个处理事件。“事件”就是点击鼠标、按下键盘、点击关闭按钮等操作。
        if event.type == pygame.QUIT: #event.type：当前事件的类型。pygame.QUIT：Pygame 中表示“请求关闭窗口”的常量，注意是大写。
            sys.exit() #退出程序

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """响应按钮"""

    if event.key == pygame.K_RIGHT:
        ship.moving_right = True

    elif event.key == pygame.K_LEFT:
        ship.moving_left = True

    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings,screen,ship,bullets)

    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event,ship):
    """响应松开"""

    if event.key == pygame.K_RIGHT:
        ship.moving_right = False

    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def update_screen(ai_settings,screen,ship,aliens,bullets):
    screen.fill(ai_settings.bg_color) #顺序很重要：先画背景，再画飞船，最后显示画面。 如果先画飞船再填满背景，飞船就会被背景盖住。

    aliens.draw(screen) #这是 Group 提供的绘制方法：读取编组中每个外星人的 image 和 rect，把图片画到指定屏幕上。 它不会调用外星人的 blitme()，而是直接使用这两个属性完成绘制。

    pygame.display.flip() #更新窗口画面


def update_bullets(bullets):
    """更新子弹位置，并移除已飞出屏幕的子弹"""

    bullets.update() #bullets 是一个编组。不仅能保存子弹，还自带一个 update() 方法，负责逐个调用成员的 update()。

    for bullet in bullets.sprites(): #遍历时如果同时修改正在遍历的容器，可能影响遍历过程。复制的是编组容器，没有复制出新的子弹。
        if bullet.rect.bottom <=0:
            bullets.remove(bullet) #修改原编组


def fire_bullet(ai_settings,screen,ship,bullets):
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings,screen,ship)
        bullets.add(new_bullet)


def get_number_aliens_x(ai_settings,alien_width):
    """计算每行可以容纳多少个外星人"""
    availble_space_x = ai_settings.screen_width - 2*alien_width
    number_aliens_x = int(availble_space_x/(2*alien_width))

    return number_aliens_x 


def get_number_rows(ai_settings,alien_height,ship_height):
    """计算屏幕可以容纳多少行外星人"""
    available_space_y = ai_settings.screen_height - 3*alien_height - ship_height
    number_rows = int(available_space_y/(2*alien_height))

    return number_rows


def create_alien(ai_settings,screen,aliens,alien_number,row_number):
    """创建一个外星人，并将其放在当前行中"""
    alien = Alien(ai_settings,screen)
    alien.x = alien.rect.width + 2*alien.rect.width*alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2*alien.rect.height*row_number #不使用alien.y的原因：外星人的垂直位置只在创建时设置一次，而且计算出来就是整数，不需要保留、累积小数
    aliens.add(alien)


def create_fleet(ai_settings,screen,aliens,ship):
    """创建外星人群"""
    alien = Alien(ai_settings,screen)

    number_aliens_x = get_number_aliens_x(ai_settings,alien.rect.width)
    number_rows = get_number_rows(ai_settings,alien.rect.height,ship.rect.height)

    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings,screen,aliens,alien_number,row_number)