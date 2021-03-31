import pygame


class Level:
    def __init__(self):
        self.location = "Plain"     # Plain, Desert, Snow
        self.spritesBackGround = pygame.sprite.Group()
        self.spritesEntity = pygame.sprite.Group()
        self.spritesEffects = pygame.sprite.Group()
        self.state = "Loading"      # Loading, Running, Closing
