import pygame


class Level:
    def __init__(self):
        self.location = 1  # 1 - Plain, 2 - Desert, 3 - Snow
        self.spritesDynamic = []
        self.spritesStatic =[]
        self.state = 1  # 1 - Loading, 2 - Running, 3 - Closing, 4 - Exit
