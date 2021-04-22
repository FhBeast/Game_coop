import pygame
import os
from entity import Entity

GAME_FOLDER = os.path.dirname(__file__)
IMG_FOLDER = os.path.join(GAME_FOLDER, 'img')

WALL_IMG = pygame.image.load(os.path.join(IMG_FOLDER, 'wall.jpg'))
BG_IMG = pygame.image.load(os.path.join(IMG_FOLDER, 'bg2.jpg'))


class ResourceLoader:
    @staticmethod
    def load_textureStatic(entities):
        entity = Entity(100, 100, 0, 0, 0, "Bg_plain", True)
        entities.append(entity)

        for entity in entities:
            entity.image = WALL_IMG
            if entity.name == "Wall":
                entity.image = WALL_IMG
            if entity.name == "Bg_plain":
                entity.image = BG_IMG
        return entities
