import pygame
from level import Level
from package import Package
import socket


class ServerManager:
    def __init__(self, port):
        self.location = 1  # 1 - Plain, 2 - Desert, 3 - Snow
        self.spritesDynamic = pygame.sprite.Group()
        self.spritesStatic = pygame.sprite.Group()
        self.state = 1  # 1 - Loading, 2 - Running, 3 - Closing, 4 - Exit
        self.__level = Level()
        self.__sock = socket.socket()
        self.__sock.bind(('', port))
        self.__sock.listen(1)

    def run(self):
        conn, addr = self.__sock.accept()

        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.send(data.upper())

        return addr
