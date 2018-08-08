#控制
import sys
import pygame
from pygame.locals import *
from bullet import Bullet
from alien import Alien
import random
import time
#键盘按下
def check_keydown_events(event,ai_setting,screen,ship,bullets):
        if event.key == pygame.K_RIGHT:
            ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            ship.moving_left = True
        elif event.key == pygame.K_UP:
            ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            ship.moving_down = True
        elif event.key==pygame.K_SPACE:
            fire_bullet(ai_setting, screen, ship, bullets)
        elif event.key==pygame.K_q:
            sys.exit()
#键盘放开
def check_keyup_events(event,ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False
 #键盘控制
def check_events(ai_setting, screen, ship, bullets,stats, play_button,aliens):
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        elif event.type==pygame.KEYDOWN:
            check_keydown_events(event,ai_setting, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type==pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y=pygame.mouse.get_pos()
            check_play_button(stats,play_button,mouse_x,mouse_y,aliens,bullets,ai_setting,screen,ship)
#按钮检测
def check_play_button(stats,play_button,mouse_x,mouse_y,aliens,bullets,setting,screen,ship):
     button_clicked=play_button.rect.collidepoint(mouse_x,mouse_y)
     if button_clicked and not stats.game_active:
        pygame.mouse.set_visible(False)
        stats.reset_stats()
        stats.game_active=True
        aliens.empty()
        bullets.empty()
        create_fleet(setting, screen, aliens)
        ship.center_ship()
#更新画布
def update_screen(setting, screen, ship, bullets, aliens,play_button,stats,sb):  #循环
    screen.fill(setting.bg_color)
    sb.show_score()
    ship.blitem()
    aliens.draw(screen)
    if not stats.game_active:
        play_button.draw_button()

    for bullet in bullets.sprites():
        bullet.draw_bullet()

    pygame.display.flip()
 #判断子弹是否飞过窗口
def update_bullets(bullets,aliens,setting,screen,stats,sb):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    collisions=pygame.sprite.groupcollide(bullets,aliens,True,True) #子弹和敌人碰撞检测
    if collisions:
        for x in collisions.values():
            stats.score+=setting.alien_points*len(aliens)
            sb.prep_score()
    if len(aliens)==0:
        bullets.empty()
        create_fleet(setting, screen, aliens)
#添加子弹
def fire_bullet(ai_setting,screen,ship,bullets):
        if  len(bullets) <= ai_setting.bullets_allowed:
            new_bullet = Bullet(ai_setting, screen, ship)
            bullets.add(new_bullet)
#创建一群敌人
def get_number_aliens_x(setting,alen_width):
    availabel_space_x = setting.screen_width - 2 *alen_width
    number_aliens_x = int(availabel_space_x / (2 * alen_width))
    return number_aliens_x
def create_alien(setting,screen,aliens,alien_number):
    alien = Alien(setting, screen)
    alien_width=alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    aliens.add(alien)
def create_fleet(setting,screen,aliens):
    alien=Alien(setting,screen)
    number_aliens_x=get_number_aliens_x(setting,alien.rect.width)
    for alien_num in range(number_aliens_x):
        create_alien(setting, screen, aliens, alien_num)
#更新敌人的位置
def update_aliens(stats, setting, screen, aliens, ship, bullets):
    aliens.update()
    if pygame.sprite.spritecollideany(ship,aliens):
        ship_hit(stats, setting, screen, aliens, ship, bullets)
    check_aliens_bottom(screen, aliens)
def ship_hit(stats,setting, screen, aliens,ship,bullets):
    #判断飞机剩余的次数
    if stats.ships_left>0:
        stats.ships_left-=1
        aliens.empty()
        bullets.empty()
        create_fleet(setting, screen, aliens)
        ship.center_ship()
        time.sleep(0.5)
    else:
        stats.game_active=False
        pygame.mouse.set_visible(True)
#检测是否有敌人到底底端
def check_aliens_bottom(screen,aliens):
    screen_rect=screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom>=screen_rect.bottom:
            aliens.remove(alien)

