import pygame
class Ship():
    def __init__(self,screen,setting):
        self.screen=screen
        self.image=pygame.image.load("image\\hero0.png")
        self.screen_rect=self.screen.get_rect()
        self.rect=self.image.get_rect()
        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom


        self.setting=setting
        ####判断方向
        self.moving_right=False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        ##更新位置
    def update(self):
        if self.moving_right and self.rect.right<=500:
            self.rect.centerx+=self.setting.ship_speed
        elif self.moving_left and self.rect.left>=0:
            self.rect.centerx-=self.setting.ship_speed
        elif self.moving_up and self.rect.top>=0:
            self.rect.bottom-=self.setting.ship_speed
        elif self.moving_down and self.rect.bottom<=800:
            self.rect.bottom+=self.setting.ship_speed

    def blitem(self):
        try:
          self.screen.blit(self.image,self.rect)
        except Exception as E:
            print(E)
    def center_ship(self):
        self.center=self.screen_rect.centerx
