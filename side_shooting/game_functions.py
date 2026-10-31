import sys

import pygame

from bullet import Bullet

def check_events(ai_settings, screen, ship, bullets, stats, play_button):
    """响应键盘和鼠标事件"""

    for event in pygame.event.get(): #逐个处理事件。“事件”就是点击鼠标、按下键盘、点击关闭按钮等操作。
        if event.type == pygame.QUIT: #event.type：当前事件的类型。pygame.QUIT：Pygame 中表示“请求关闭窗口”的常量，注意是大写。
            sys.exit() #退出程序

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets,stats)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y = pygame.mouse.get_pos()
            check_play_button(bullets,stats,play_button,mouse_x,mouse_y)


def check_keydown_events(event, ai_settings, screen, ship, bullets,stats):
    """响应按钮"""

    if event.key == pygame.K_DOWN:
        ship.moving_down = True

    elif event.key == pygame.K_UP:
        ship.moving_up = True

    elif event.key == pygame.K_SPACE:
        if stats.game_active:
            fire_bullet(ai_settings,screen,ship,bullets)


def check_keyup_events(event,ship):
    """响应松开"""

    if event.key == pygame.K_DOWN:
        ship.moving_down = False

    elif event.key == pygame.K_UP:
        ship.moving_up = False


def update_screen(ai_settings,screen,ship,bullets,target,stats,play_button):
    screen.fill(ai_settings.bg_color) #顺序很重要：先画背景，再画飞船，最后显示画面。 如果先画飞船再填满背景，飞船就会被背景盖住。

    for bullet in bullets.sprites(): #sprites() 是 Pygame 的 Group 类已经提供的方法，作用是返回编组中所有精灵对象组成的列表。
        bullet.draw_bullet()

    ship.blitme()

    target.draw_target()

    #游戏未开始或已结束时，显示按钮
    if not stats.game_active:
        play_button.draw_button()

    pygame.display.flip() #更新窗口画面


def update_bullets(bullets,stats):
    """更新子弹位置，并移除已飞出屏幕的子弹"""

    bullets.update() #bullets 是一个编组。不仅能保存子弹，还自带一个 update() 方法，负责逐个调用成员的 update()。

    for bullet in bullets.sprites(): #遍历时如果同时修改正在遍历的容器，可能影响遍历过程。复制的是编组容器，没有复制出新的子弹。
        if bullet.rect.left >= bullet.screen.get_rect().right:
            bullets.remove(bullet) #修改原编组

            stats.missed_shots += 1
            print(f"未命中次数：{stats.missed_shots}")

            if stats.missed_shots >= 3:
                stats.game_active = False #注意，设置 game_active = False 本身不会立即中断循环。主程序下一轮读到这个值时，才会跳过更新位置的代码。
                break #break 退出当前 for，不再检查这一轮剩余的子弹。


def check_bullet_target_collision(bullets,target):
    """检查子弹是否击中目标"""
    for bullet in bullets.copy():
        if bullet.rect.colliderect(target.rect): #这里的新方法用来检查两个矩形是否重叠：重叠，返回True，执行删除子弹和打印；不重叠，返回False.
            bullets.remove(bullet)
            target.reset_position()
            break #注意：它只能避免同一轮遍历中连续命中。也可以不加

def fire_bullet(ai_settings,screen,ship,bullets):
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings,screen,ship)
        bullets.add(new_bullet)


def check_play_button(bullets,stats,play_button,mouse_x,mouse_y):
    """点击Play按钮时启动游戏"""

    button_clicked = play_button.rect.collidepoint(mouse_x,mouse_y)

    if button_clicked and not stats.game_active:
        stats.reset_stats()
        bullets.empty()
        stats.game_active = True