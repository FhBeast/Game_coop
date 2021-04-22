import pygame
from level import Level
import socket
import pickle
from clientPackage import ClientPackage
from Server.levelLoader import LevelLoader


class ServerManager:
    def __init__(self, port):
        self.__level = Level()
        self.__collidingObjects = []
        self.__sock = socket.socket()
        self.__sock.bind(('', port))
        self.__sock.listen(1)
        self.__level = LevelLoader.load_level(0)

    def run(self):
        conn, addr = self.__sock.accept()

        while True:
            data = conn.recv(8192)
            if not data:
                break

            data = pickle.loads(data)
            self.__level.state = data.state
            left = data.left
            right = data.right
            jump = data.jump
            attack = data.attack

            if self.__level.state == 1:
                for entity in self.__level.spritesStatic:
                    if entity.collide:
                        self.__collidingObjects.append(entity)
                for entity in self.__level.spritesDynamic:
                    if entity.collide:
                        self.__collidingObjects.append(entity)

            for entity in self.__level.spritesDynamic:
                if entity.name == "Player":
                    entity.update(left, right, jump, attack, self.__collidingObjects)

            level = self.__level
            data = pickle.dumps(level)

            conn.send(data)

        conn.close()
        return addr
