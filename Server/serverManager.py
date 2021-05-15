import time

import pygame
from level import Level
import socket
import pickle
import threading
from Server.levelLoader import LevelLoader


class ServerManager:
    def __init__(self, port):
        self.__level = Level()
        self.__collidingObjects = []
        self.__sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__sock.bind(('', port))
        self.__sock.listen(2)
        self.__loadingLevel = False
        self.__serverRunning = True
        self.__clock = pygame.time.Clock()
        self.__tickRate = 60
        self.__clientData = bytes()
        self.__clientData2 = bytes()
        self.__serverData = bytes()

        self.__level = LevelLoader.load_level(0)

    def update(self):
        while True:
            self.__clock.tick(self.__tickRate)
            if not (self.__clientData and self.__clientData2):
                continue

            data = pickle.loads(self.__clientData)
            data2 = pickle.loads(self.__clientData2)
            left_one = data.left
            right_one = data.right
            jump_one = data.jump
            attack_one = data.attack
            left_two = data2.left
            right_two = data2.right
            jump_two = data2.jump
            attack_two = data2.attack

            if not self.__loadingLevel:
                self.__collidingObjects.clear()
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
                        entity.update(left_one, right_one, jump_one, self.__collidingObjects)
                    elif entity.playerId == 2:
                        entity.update(left_two, right_two, jump_two, self.__collidingObjects)

            self.__serverData = pickle.dumps(self.__level)

        return

    def data_receiving(self):
        conn, addr = self.__sock.accept()
        conn2, addr2 = self.__sock.accept()
        while self.__serverRunning:
            self.__clientData = conn.recv(8192)
            self.__clientData2 = conn2.recv(8192)
            while not self.__loadingLevel:
                time.sleep(0.1)
            conn.send(self.__serverData)
            conn2.send(self.__serverData)
        conn.close()
        conn2.close()

    def run(self):
        thread_update = threading.Thread(target=self.update)
        thread_data_receiving = threading.Thread(target=self.data_receiving)

        thread_update.start()
        thread_data_receiving.start()

        thread_update.join()
        thread_data_receiving.join()
