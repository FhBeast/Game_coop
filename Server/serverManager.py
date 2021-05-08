import pygame
from level import Level
import socket
import pickle
from Server.levelLoader import LevelLoader


class ServerManager:
    def __init__(self, port):
        self.__level = Level()
        self.__collidingObjects = []
        self.__sock = socket.socket()
        self.__sock.bind(('', port))
        self.__sock.listen(2)
        self.__loadingLevel = False

        self.__level = LevelLoader.load_level(0)

    def run(self):
        conn, addr = self.__sock.accept()
        conn2, addr2 = self.__sock.accept()

        while True:
            data = conn.recv(8192)
            data2 = conn2.recv(8192)
            if not data:
                break

            data = pickle.loads(data)
            data2 = pickle.loads(data2)
            left_one = data.left
            right_one = data.right
            jump_one = data.jump
            attack_one = data.attack
            left_two = data2.left
            right_two = data2.right
            jump_two = data2.jump
            attack_two = data2.attack

            if not self.__loadingLevel:
                for entity in self.__level.spritesStatic:
                    if entity.collide:
                        self.__collidingObjects.append(entity)
                for entity in self.__level.spritesDynamic:
                    if entity.collide:
                        self.__collidingObjects.append(entity)
                self.__loadingLevel = True

            for entity in self.__level.spritesDynamic:
                if entity.name == "Player":
                    if entity.playerId == 1:
                        entity.update(left_one, right_one, jump_one, attack_one, self.__collidingObjects)
                    elif entity.playerId == 2:
                        entity.update(left_two, right_two, jump_two, attack_two, self.__collidingObjects)

            level = self.__level
            data = pickle.dumps(level)
            conn.send(data)
            conn2.send(data)

        conn.close()
        return
