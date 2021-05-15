import pygame
import os
from entity import Entity

GAME_FOLDER = os.path.dirname(__file__)
IMG_FOLDER = os.path.join(GAME_FOLDER, 'img')

WALL_IMG = pygame.image.load(os.path.join(IMG_FOLDER, 'wall.jpg'))
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

    @staticmethod
    def load_textureDynamic(entities):
        for entity in entities:
            entity.image = WALL_IMG
            if entity.name == "Player":
                if entity.playerId == 1:
                    if entity.lookRight:
                        if entity.state == 0:
                            entity.image = ANIMATION_STAY_RIGHT
                        if entity.state == 1:
                            entity.image = ANIMATION_JUMP_RIGHT
                        if entity.state == 2:
                            entity.image = ANIMATION_RUN_RIGHT[int(entity.frame)]
                    else:
                        if entity.state == 0:
                            entity.image = ANIMATION_STAY_LEFT
                        if entity.state == 1:
                            entity.image = ANIMATION_JUMP_LEFT
                        if entity.state == 2:
                            entity.image = ANIMATION_RUN_LEFT[int(entity.frame)]
                else:
                    if entity.lookRight:
                        if entity.state == 0:
                            entity.image = ANIMATION2_STAY_RIGHT
                        if entity.state == 1:
                            entity.image = ANIMATION2_JUMP_RIGHT
                        if entity.state == 2:
                            entity.image = ANIMATION2_RUN_RIGHT[int(entity.frame)]
                    else:
                        if entity.state == 0:
                            entity.image = ANIMATION2_STAY_LEFT
                        if entity.state == 1:
                            entity.image = ANIMATION2_JUMP_LEFT
                        if entity.state == 2:
                            entity.image = ANIMATION2_RUN_LEFT[int(entity.frame)]

        return entities
