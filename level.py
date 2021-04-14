import pygame


class Level:
    def __init__(self):
        self.location = "Plain"     # Plain, Desert, Snow
        self.spritesDynamic = pygame.sprite.Group()
        self.spritesStatic = pygame.sprite.Group()
        self.state = "Loading"      # Loading, Running, Closing
