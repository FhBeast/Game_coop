import pygame
import socket
import pickle
from resourceLoader import ResourceLoader
from clientPackage import ClientPackage
from operator import attrgetter


class ClientManager:
    def __init__(self):
        self.__spritesDynamic = []
        self.__spritesStatic = []
        self.__sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__sock.connect(('localhost', 9090))
        self.__package = ClientPackage()
        self.__state = 1
        self.__number = -1

    def update_objects(self, control):
        left = right = False
        jump = False
        use = False
        attack = False

        if control[pygame.K_a]:
            left = True
        if control[pygame.K_d]:
            right = True
        if control[pygame.K_w]:
            jump = True

        self.__package.left = left
        self.__package.right = right
        self.__package.jump = jump
        self.__sock.send(pickle.dumps(self.__package))
        data = self.__sock.recv(8192)
        data = pickle.loads(data)
        if data.number == self.__number:
            self.__spritesDynamic = data.spritesDynamic
            self.__spritesDynamic = ResourceLoader.load_textureDynamic(self.__spritesDynamic)
        else:
            self.__spritesStatic = data.spritesStatic
            self.__spritesStatic = ResourceLoader.load_textureStatic(self.__spritesStatic)
            self.__spritesDynamic = data.spritesDynamic
            self.__spritesDynamic = ResourceLoader.load_textureDynamic(self.__spritesDynamic)
            data.number = self.__number

        entities = self.__spritesStatic + self.__spritesDynamic
        sprites = pygame.sprite.Group()
        for entity in sorted(entities, key=attrgetter('layer')):
            sprites.add(entity)
        return sprites

    def __disconnect(self):
        self.__sock.close()
