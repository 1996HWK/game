import pygame
from settings import Setting
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
def run_game():
    setting=Setting()
    pygame.init()
    screen=pygame.display.set_mode([setting.screen_width,setting.screen_height])
    pygame.display.set_caption("飞机大战")

    ship = Ship(screen,setting)
    bullets = Group()
    aliens = Group()
    gf.create_fleet(setting, screen, aliens)
    stats = GameStats(setting)
    sb=Scoreboard(setting,screen,stats)
    play_button=Button(setting,screen,"Play")

    while True:

           gf.check_events(setting, screen, ship, bullets,stats, play_button,aliens)
           if stats.game_active:
                ship.update()
                gf.update_bullets(bullets, aliens, setting, screen,stats,sb)
                gf.update_aliens(stats, setting, screen, aliens, ship, bullets)
           gf.update_screen(setting, screen, ship, bullets, aliens,play_button,stats,sb)

if __name__=="__main__":
    run_game()