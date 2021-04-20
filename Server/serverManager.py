import pygame
from level import Level
import socket


class ServerManager:
    def __init__(self, port):
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
