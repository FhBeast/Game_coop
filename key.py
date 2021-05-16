import pygame
from entity import Entity

KEY_WIDTH = 34
KEY_HEIGHT = 18

KEY_X = 50 - (KEY_WIDTH / 2)
KEY_Y = 70 - (KEY_HEIGHT / 2)


class Key(Entity):

    def __init__(self, x, y):
        Entity.__init__(self, x, y, KEY_WIDTH, KEY_HEIGHT, 3, "Key", False)
        self.rect = pygame.Rect(x + KEY_X, y + KEY_Y, KEY_WIDTH, KEY_HEIGHT)

    def picked(self):
        self.kill()
