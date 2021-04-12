import pygame


class ServerManager:
    def __init__(self):
        self.__spritesDynamic = pygame.sprite.Group()
        self.__spritesStatic = pygame.sprite.Group()
