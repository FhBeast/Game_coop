import pygame
from level import Level

WALL_WIDTH = 100
WALL_HEIGHT = 100

PLATFORM_WIDTH = WALL_WIDTH
PLATFORM_HEIGHT = 30

WALL = "="
PLATFORM = "-"
PLAYER = "P"
DOOR = "D"
DOOR_LOCKED = "L"
KEY = "K"
SHRUB = "*"
BOX = "B"
STONE = "#"
STONE_SMALL = "_"
CRYSTAL = "+"


class LevelLoader:
    @staticmethod
    def load_level(number):
        level = Level()

        file = open('levels.txt')
        for line in file:
            if line[0] == "/":
                number -= 1
            if number == 0:
                if line[1] == "p":
                    level.location = "Plain"

                x = y = 0
                for row in range(14):
                    for col in range(len(line)):
                        pass
