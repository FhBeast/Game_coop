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

            level = self.__level
            data = pickle.dumps(level)

            conn.send(data)

        conn.close()
        return addr
