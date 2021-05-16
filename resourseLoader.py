import pygame
import os
from entity import Entity

GAME_FOLDER = os.path.dirname(__file__)
IMG_FOLDER = os.path.join(GAME_FOLDER, 'img')

NONE = pygame.image.load(os.path.join(IMG_FOLDER, 'none.png'))

WALL_IMG = pygame.image.load(os.path.join(IMG_FOLDER, 'wall.jpg'))
WALL_GRASS_IMG = pygame.image.load(os.path.join(IMG_FOLDER, 'wall_grass.jpg'))

PLATFORM_SINGLE = pygame.image.load(os.path.join(IMG_FOLDER, 'platform_single.png'))
PLATFORM_RIGHT = pygame.image.load(os.path.join(IMG_FOLDER, 'platform_right.png'))
PLATFORM_LEFT = pygame.image.load(os.path.join(IMG_FOLDER, 'platform_left.png'))
PLATFORM_CENTER = pygame.image.load(os.path.join(IMG_FOLDER, 'platform_center.png'))

SHRUB = pygame.image.load(os.path.join(IMG_FOLDER, 'shrub.png'))

STONE = pygame.image.load(os.path.join(IMG_FOLDER, 'stone.png'))
STONE_SMALL = pygame.image.load(os.path.join(IMG_FOLDER, 'stone_small.png'))

KEY = pygame.image.load(os.path.join(IMG_FOLDER, 'key.png'))

BG_IMG = pygame.image.load(os.path.join(IMG_FOLDER, 'bg2.jpg'))

ANIMATION_STAY_RIGHT = pygame.image.load(os.path.join(IMG_FOLDER, 'idle.png'))
ANIMATION_STAY_LEFT = pygame.transform.flip(ANIMATION_STAY_RIGHT, True, False)
ANIMATION_JUMP_RIGHT = pygame.image.load(os.path.join(IMG_FOLDER, 'idle_jump.png'))
ANIMATION_JUMP_LEFT = pygame.transform.flip(ANIMATION_JUMP_RIGHT, True, False)
ANIMATION_RUN_RIGHT = [pygame.image.load(os.path.join(IMG_FOLDER, 'idle_run.png')),
                       pygame.image.load(os.path.join(IMG_FOLDER, 'idle_run2.png')),
                       pygame.image.load(os.path.join(IMG_FOLDER, 'idle_run3.png')),
                       pygame.image.load(os.path.join(IMG_FOLDER, 'idle_run4.png')),
                       pygame.image.load(os.path.join(IMG_FOLDER, 'idle_run5.png')),
                       pygame.image.load(os.path.join(IMG_FOLDER, 'idle_run6.png'))]
ANIMATION_RUN_LEFT = [pygame.transform.flip(image, True, False) for image in ANIMATION_RUN_RIGHT]
ANIMATION2_STAY_RIGHT = pygame.image.load(os.path.join(IMG_FOLDER, 'idle2.png'))
ANIMATION2_STAY_LEFT = pygame.transform.flip(ANIMATION2_STAY_RIGHT, True, False)
ANIMATION2_JUMP_RIGHT = pygame.image.load(os.path.join(IMG_FOLDER, 'idle2_jump.png'))
ANIMATION2_JUMP_LEFT = pygame.transform.flip(ANIMATION2_JUMP_RIGHT, True, False)
ANIMATION2_RUN_RIGHT = [pygame.image.load(os.path.join(IMG_FOLDER, 'idle2_run.png')),
                        pygame.image.load(os.path.join(IMG_FOLDER, 'idle2_run2.png')),
                        pygame.image.load(os.path.join(IMG_FOLDER, 'idle2_run3.png')),
                        pygame.image.load(os.path.join(IMG_FOLDER, 'idle2_run4.png')),
                        pygame.image.load(os.path.join(IMG_FOLDER, 'idle2_run5.png')),
                        pygame.image.load(os.path.join(IMG_FOLDER, 'idle2_run6.png'))]
ANIMATION2_RUN_LEFT = [pygame.transform.flip(image, True, False) for image in ANIMATION2_RUN_RIGHT]

DOOR_1 = pygame.image.load(os.path.join(IMG_FOLDER, 'door1.png'))
DOOR_2 = pygame.image.load(os.path.join(IMG_FOLDER, 'door2.png'))
DOOR_1_LOCKED = pygame.image.load(os.path.join(IMG_FOLDER, 'door1_locked.png'))
DOOR_2_LOCKED = pygame.image.load(os.path.join(IMG_FOLDER, 'door2_locked.png'))


class ResourceLoader:
    @staticmethod
    def load_textureStatic(entities):
        entity = Entity(100, 100, 0, 0, 0, "Bg_plain", True)
        entities.append(entity)

        for entity in entities:
            entity.image = NONE
            if entity.name == "Wall":
                entity.image = WALL_IMG
            elif entity.name == "WallGrass":
                entity.image = WALL_GRASS_IMG
            elif entity.name == "Platform0":
                entity.image = PLATFORM_SINGLE
            elif entity.name == "Platform1":
                entity.image = PLATFORM_RIGHT
            elif entity.name == "Platform2":
                entity.image = PLATFORM_LEFT
            elif entity.name == "Platform3":
                entity.image = PLATFORM_CENTER
            elif entity.name == "Shrub":
                entity.image = SHRUB
            elif entity.name == "Stone":
                entity.image = STONE
            elif entity.name == "StoneSmall":
                entity.image = STONE_SMALL
            elif entity.name == "Key":
                entity.image = KEY
            elif entity.name == "Bg_plain":
                entity.image = BG_IMG
        return entities

    @staticmethod
    def load_textureDynamic(entities):
        for entity in entities:
            entity.image = NONE
            if entity.name == "Door":
                if entity.playerId == 1:
                    if entity.is_locked:
                        entity.image = DOOR_1_LOCKED
                    else:
                        entity.image = DOOR_1
                else:
                    if entity.is_locked:
                        entity.image = DOOR_2_LOCKED
                    else:
                        entity.image = DOOR_2
            elif entity.name == "Player":
                if entity.playerId == 1:
                    if entity.lookRight:
                        if entity.state == 0:
                            entity.image = ANIMATION_STAY_RIGHT
                        elif entity.state == 1:
                            entity.image = ANIMATION_JUMP_RIGHT
                        elif entity.state == 2:
                            entity.image = ANIMATION_RUN_RIGHT[int(entity.frame)]
                    else:
                        if entity.state == 0:
                            entity.image = ANIMATION_STAY_LEFT
                        elif entity.state == 1:
                            entity.image = ANIMATION_JUMP_LEFT
                        elif entity.state == 2:
                            entity.image = ANIMATION_RUN_LEFT[int(entity.frame)]
                else:
                    if entity.lookRight:
                        if entity.state == 0:
                            entity.image = ANIMATION2_STAY_RIGHT
                        elif entity.state == 1:
                            entity.image = ANIMATION2_JUMP_RIGHT
                        elif entity.state == 2:
                            entity.image = ANIMATION2_RUN_RIGHT[int(entity.frame)]
                    else:
                        if entity.state == 0:
                            entity.image = ANIMATION2_STAY_LEFT
                        elif entity.state == 1:
                            entity.image = ANIMATION2_JUMP_LEFT
                        elif entity.state == 2:
                            entity.image = ANIMATION2_RUN_LEFT[int(entity.frame)]

        return entities
