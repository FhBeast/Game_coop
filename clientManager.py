import pygame
import socket
import pickle
from resourseLoader import ResourceLoader
from clientPackage import ClientPackage
from operator import attrgetter


class ClientManager:
    def __init__(self):
        self.__spritesDynamic = []
        self.__spritesStatic = []
        self.__sock = socket.socket()
        self.__sock.connect(('localhost', 9090))
        self.__package = ClientPackage()

    def update_objects(self, control):
        self.__package.control = control
        self.__sock.send(pickle.dumps(self.__package))
        data = self.__sock.recv(8192)
        data = pickle.loads(data)
        if data.state == 1:
            self.__spritesStatic = data.spritesStatic
            self.__spritesStatic = ResourceLoader.load_textureStatic(self.__spritesStatic)
            self.__package.state = 2

        entities = self.__spritesStatic + self.__spritesDynamic
        sprites = pygame.sprite.Group()
        for entity in sorted(entities, key=attrgetter('layer')):
            sprites.add(entity)
        return sprites

    def __disconnect(self):
        self.__sock.close()
