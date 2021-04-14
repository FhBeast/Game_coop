import pygame


class Package:
    def __init__(self):
        self.location = 1  # 1 - Plain, 2 - Desert, 3 - Snow
        self.spritesDynamic = pygame.sprite.Group()
        self.spritesStatic = pygame.sprite.Group()
        self.state = 1  # 1 - Loading, 2 - Running, 3 - Closing, 4 - Exit
