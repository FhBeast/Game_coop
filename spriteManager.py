import pygame


class SpriteManager:
    def __init__(self):
        self.spritesBackGround = pygame.sprite.Group()
        self.spritesEntity = pygame.sprite.Group()
        self.spritesEffects = pygame.sprite.Group()

    def update_objects(self):
        sprites = pygame.sprite.Group()
        return sprites
