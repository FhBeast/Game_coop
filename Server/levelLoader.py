# import pygame
from level import Level
from entity import Entity
from player import Player
from door import Door
from key import Key

WALL_WIDTH = 100
WALL_HEIGHT = 100

PLATFORM_WIDTH = WALL_WIDTH
PLATFORM_HEIGHT = 30

WALL = "="
PLATFORM = "-"
PLAYER_1 = "1"
PLAYER_2 = "2"
DOOR_1 = "R"            # NO FUNCTIONALITY
DOOR_2 = "B"            # NO FUNCTIONALITY
DOOR_1_LOCKED = "r"     # NO FUNCTIONALITY
DOOR_2_LOCKED = "b"     # NO FUNCTIONALITY
KEY = "K"               # NO
SHRUB = "*"
BOX = "B"               # NO
STONE = "#"
STONE_SMALL = "_"
CRYSTAL = "+"           # NO


class LevelLoader:
    @staticmethod
    def load_level(number):
        level = Level()

        file = open('levels.txt')

        loading = False
        pre_line = "=============="

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
                    # ===================================================================
                    if line[col] == WALL:
                        if pre_line[col] != WALL:
                            entity = Entity(x, y, WALL_WIDTH, WALL_HEIGHT, 1, "WallGrass", True)
                        else:
                            entity = Entity(x, y, WALL_WIDTH, WALL_HEIGHT, 1, "Wall", True)
                        level.spritesStatic.append(entity)
                    elif line[col] == PLATFORM:
                        variant = 0
                        if col:
                            if line[col - 1] == PLATFORM or line[col - 1] == WALL:
                                variant += 1
                        if col + 1 != len(line):
                            if line[col + 1] == PLATFORM or line[col + 1] == WALL:
                                variant += 2
                        platform = Entity(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT, 1, "Platform" + str(variant), True)
                        level.spritesStatic.append(platform)
                    elif line[col] == SHRUB:
                        entity = Entity(x, y, WALL_WIDTH, WALL_HEIGHT, 3, "Shrub", False)
                        level.spritesStatic.append(entity)
                    elif line[col] == STONE:
                        entity = Entity(x, y, WALL_WIDTH, WALL_HEIGHT, 1, "Stone", True)
                        level.spritesStatic.append(entity)
                    elif line[col] == STONE_SMALL:
                        entity = Entity(x, y + 70, WALL_WIDTH, 30, 1, "StoneSmall", True)
                        level.spritesStatic.append(entity)
                    elif line[col] == KEY:
                        key = Key(x, y)
                        level.spritesDynamic.append(key)
                    elif line[col] == PLAYER_1:
                        player = Player(x, y, 1)
                        level.spritesDynamic.append(player)
                    elif line[col] == PLAYER_2:
                        player = Player(x, y, 2)
                        level.spritesDynamic.append(player)
                    elif line[col] == DOOR_1:
                        door = Door(x, y, 1, False)
                        level.spritesDynamic.append(door)
                    elif line[col] == DOOR_2:
                        door = Door(x, y, 2, False)
                        level.spritesDynamic.append(door)
                    elif line[col] == DOOR_1_LOCKED:
                        door = Door(x, y, 1, True)
                        level.spritesDynamic.append(door)
                    elif line[col] == DOOR_2_LOCKED:
                        door = Door(x, y, 2, True)
                        level.spritesDynamic.append(door)
                    # ===================================================================
                    x += WALL_WIDTH
                pre_line = line
                y += WALL_HEIGHT

        return level
