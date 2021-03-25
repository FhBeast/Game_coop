import pygame


class Entity(pygame.sprite.Sprite):

    def __init__(self, x, y, width, height, layer, name, collide):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((width, height))
        self.rect = pygame.Rect(x, y, width, height)
        self.layer = layer
        self.name = name
        self.collide = collide
