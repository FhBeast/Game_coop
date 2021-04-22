# import pygame
from level import Level
from entity import Entity

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

        loading = False

        y = 0
        for line in file:
            if line[0] == "":
                break
            elif line[0] == "/":
                if number == 0:
                    loading = True
                    if line[1] == "p":
                        level.location = "Plain"
                elif number == -1:
                    break
                number -= 1
            elif loading:
                x = 0
                for col in range(len(line)):
                    if line[col] == WALL:
                        entity = Entity(x, y, WALL_WIDTH, WALL_HEIGHT, 1, "Wall", True)
                        level.spritesStatic.append(entity)
                    x += WALL_WIDTH
                y += WALL_HEIGHT

        return level
