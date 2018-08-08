import pygame
from pygame.sprite import  Sprite
class Alien(Sprite):
    def __init__(self,ai_settings,screen):

        super(Alien,self).__init__()
        self.screen=screen
        self.ai_settings=ai_settings
        self.image=pygame.image.load("image\\aline1.png")
        self.rect=self.image.get_rect()
        self.speed_factor=self.ai_settings.alien_speed_factor
        self.rect.x=self.rect.width
        self.rect.y=self.rect.height
        self.y=float(self.rect.y)
    def update(self):
        self.y+=self.speed_factor
        self.rect.y=self.y
    def blitme(self):
        self.screen.blit(self.image,self.rect)