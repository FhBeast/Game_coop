import time

import pygame
from level import Level
import socket
import pickle
import threading
from Server.levelLoader import LevelLoader
from player import Player
from door import Door
from key import Key


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
        self.__levelNumber = 0
        self.__playerFirst = Player
        self.__playerSecond = Player
        self.__level = LevelLoader.load_level(self.__levelNumber)

    def update(self):
        while True:
            self.__clock.tick(self.__tickRate)
            while not (self.__clientData and self.__clientData2):
                time.sleep(0.1)

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
                    if isinstance(entity, Player):
                        if entity.playerId == 1:
                            self.__playerFirst = entity
                        elif entity.playerId == 2:
                            self.__playerSecond = entity
                self.__loadingLevel = True

            exit_first = False
            exit_second = False
            self.__playerFirst.update(left_one, right_one, jump_one, self.__collidingObjects)
            self.__playerSecond.update(left_two, right_two, jump_two, self.__collidingObjects)
            for entity in self.__level.spritesDynamic:
                if isinstance(entity, Door):
                    if entity.is_locked:
                        if self.__playerFirst.key and pygame.sprite.collide_rect(self.__playerFirst, entity):
                            entity.is_locked = False
                            self.__playerFirst.key = False
                        elif self.__playerSecond.key and pygame.sprite.collide_rect(self.__playerSecond, entity):
                            entity.is_locked = False
                            self.__playerSecond.key = False
                    else:
                        if entity.playerId == 1 and pygame.sprite.collide_rect(self.__playerFirst, entity):
                            exit_first = True
                        elif entity.playerId == 2 and pygame.sprite.collide_rect(self.__playerSecond, entity):
                            exit_second = True
                if isinstance(entity, Key):
                    if pygame.sprite.collide_rect(self.__playerFirst, entity) and not self.__playerFirst.key:
                        self.__playerFirst.key = True
                        entity.picked()
                        self.__level.spritesDynamic.remove(entity)
                    elif pygame.sprite.collide_rect(self.__playerSecond, entity) and not self.__playerSecond.key:
                        self.__playerSecond.key = True
                        entity.picked()
                        self.__level.spritesDynamic.remove(entity)

            if self.__playerFirst.rect.top > 1000:
                self.restart_level()
            elif self.__playerSecond.rect.top > 1000:
                self.restart_level()

            if exit_first and exit_second:
                self.next_level()

            self.__serverData = pickle.dumps(self.__level)

    def restart_level(self):
        self.__loadingLevel = False
        self.__level = LevelLoader.load_level(self.__levelNumber)

    def next_level(self):
        self.__levelNumber += 1
        self.__loadingLevel = False
        self.__level = LevelLoader.load_level(self.__levelNumber)

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
