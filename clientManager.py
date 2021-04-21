import pygame
import os
import socket
import pickle
from Server.levelLoader import LevelLoader

GAME_FOLDER = os.path.dirname(__file__)
IMG_FOLDER = os.path.join(GAME_FOLDER, 'img')

WALL_IMG = pygame.image.load(os.path.join(IMG_FOLDER, 'wall.jpg'))


class ClientManager:
    def __init__(self):
        self.__spritesDynamic = pygame.sprite.Group()
        self.__spritesStatic = pygame.sprite.Group()
        self.__sock = socket.socket()
        self.__sock.connect(('localhost', 9090))
        # ================= TEST ====================
        self.level = LevelLoader.load_level(0)
        for sprite in self.level.spritesStatic.sprites():
            sprite.image = WALL_IMG
        for sprite in self.level.spritesStatic:
            self.__spritesStatic.add(sprite)
        # ===========================================

    def update_objects(self, control):
        self.__sock.send(pickle.dumps(control))
        data = self.__sock.recv(1024)
        data = pickle.loads(data)

        return self.__spritesStatic

    def __disconnect(self):
        self.__sock.close()
