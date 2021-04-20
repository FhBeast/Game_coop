import pygame
import os
from Server.levelLoader import LevelLoader

GAME_FOLDER = os.path.dirname(__file__)
IMG_FOLDER = os.path.join(GAME_FOLDER, 'img')

WALL_IMG = pygame.image.load(os.path.join(IMG_FOLDER, 'wall.jpg'))


class ClientManager:
    def __init__(self):
        self.__spritesDynamic = pygame.sprite.Group()
        self.__spritesStatic = pygame.sprite.Group()
        # ================= TEST ====================
        self.level = LevelLoader.load_level(0)
        for sprite in self.level.spritesStatic.sprites():
            sprite.image = WALL_IMG
        for sprite in self.level.spritesStatic:
            self.__spritesStatic.add(sprite)
        # ===========================================

    def update_objects(self, control):

        return self.__spritesStatic
